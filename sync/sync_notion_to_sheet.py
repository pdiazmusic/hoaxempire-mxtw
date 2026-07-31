"""
Sincroniza la base de datos 'Tareas' de Notion hacia la pestaña 'Tareas'
del Google Sheet del asistente MXTW. Notion es la fuente de verdad para
tareas; este script sobrescribe la pestaña Tareas del Sheet en cada corrida.

Variables de entorno requeridas (se configuran como GitHub Secrets):
  NOTION_TOKEN              -> token de la integración interna de Notion
  NOTION_TAREAS_DB_ID       -> ID de la base de datos "Tareas" en Notion
  GCP_SERVICE_ACCOUNT_JSON  -> el mismo JSON de la cuenta de servicio de Google
  SHEET_NAME (opcional)     -> nombre del Google Sheet (default: "MXTW Asistente - Datos")
"""
import os
import json
from notion_client import Client
import gspread
from google.oauth2.service_account import Credentials

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
NOTION_DB_ID = os.environ["NOTION_TAREAS_DB_ID"]
GCP_JSON = os.environ["GCP_SERVICE_ACCOUNT_JSON"]
SHEET_NAME = os.environ.get("SHEET_NAME", "MXTW Asistente - Datos")

ESTADO_MAP = {
    "Sin empezar": "Pendiente",
    "En curso": "En progreso",
    "Listo": "Resuelto",
}


def get_notion_tasks(notion):
    tasks = []
    cursor = None
    while True:
        kwargs = {"database_id": NOTION_DB_ID}
        if cursor:
            kwargs["start_cursor"] = cursor
        resp = notion.databases.query(**kwargs)
        for page in resp["results"]:
            props = page["properties"]

            title_parts = props.get("Tarea", {}).get("title", [])
            tarea = "".join([t.get("plain_text", "") for t in title_parts]).strip()
            if not tarea:
                continue  # ignora filas sin nombre de tarea

            casa_prop = props.get("Casa", {}).get("select")
            casa = casa_prop["name"] if casa_prop else "General / Todas las casas"

            estado_prop = props.get("Estado", {}).get("status")
            estado_raw = estado_prop["name"] if estado_prop else "Sin empezar"
            estado = ESTADO_MAP.get(estado_raw, estado_raw)

            resp_prop = props.get("Responsable", {}).get("select")
            responsable = resp_prop["name"] if resp_prop else "Sin asignar"

            date_prop = props.get("Fecha límite", {}).get("date")
            fecha = date_prop["start"] if date_prop else ""

            tasks.append([casa, tarea, estado, fecha, responsable])

        if resp.get("has_more"):
            cursor = resp.get("next_cursor")
        else:
            break
    return tasks


def main():
    notion = Client(auth=NOTION_TOKEN)

    creds_dict = json.loads(GCP_JSON, strict=False)
    scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
    gc = gspread.authorize(creds)

    sh = gc.open(SHEET_NAME)
    ws = sh.worksheet("Tareas")

    tasks = get_notion_tasks(notion)

    ws.clear()
    ws.append_row(["Casa", "Tarea", "Estado", "Fecha_limite", "Responsable"])
    for row in tasks:
        ws.append_row(row)

    print(f"Sincronizadas {len(tasks)} tarea(s) desde Notion hacia el Sheet.")


if __name__ == "__main__":
    main()
