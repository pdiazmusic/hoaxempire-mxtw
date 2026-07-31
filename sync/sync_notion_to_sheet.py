"""
Sincroniza la base de datos 'Tareas' de Notion hacia la pestaña 'Tareas'
del Google Sheet del asistente MXTW. Notion es la fuente de verdad para
tareas; este script sobrescribe la pestaña Tareas del Sheet en cada corrida.

Usa la API REST de Notion directamente (sin la librería notion-client),
fijada a la versión de API 2022-06-28, para evitar romperse cada vez que
notion-client cambia su forma de consultar bases de datos.

Variables de entorno requeridas (se configuran como GitHub Secrets):
  NOTION_TOKEN              -> token de la integración interna de Notion
  NOTION_TAREAS_DB_ID       -> ID de la base de datos "Tareas" en Notion
  GCP_SERVICE_ACCOUNT_JSON  -> el mismo JSON de la cuenta de servicio de Google
  SHEET_NAME (opcional)     -> nombre del Google Sheet (default: "MXTW Asistente - Datos")
"""
import os
import json
import requests
import gspread
from google.oauth2.service_account import Credentials

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
NOTION_DB_ID = os.environ["NOTION_TAREAS_DB_ID"]
GCP_JSON = os.environ["GCP_SERVICE_ACCOUNT_JSON"]
SHEET_NAME = os.environ.get("SHEET_NAME", "MXTW Asistente - Datos")

NOTION_API_VERSION = "2022-06-28"
NOTION_HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": NOTION_API_VERSION,
    "Content-Type": "application/json",
}

ESTADO_MAP = {
    "Sin empezar": "Pendiente",
    "En curso": "En progreso",
    "Listo": "Resuelto",
}


def get_notion_tasks():
    tasks = []
    cursor = None
    url = f"https://api.notion.com/v1/databases/{NOTION_DB_ID}/query"

    while True:
        payload = {}
        if cursor:
            payload["start_cursor"] = cursor

        r = requests.post(url, headers=NOTION_HEADERS, json=payload, timeout=30)
        if not r.ok:
            raise RuntimeError(f"Notion API error {r.status_code}: {r.text}")
        resp = r.json()

        for page in resp.get("results", []):
            props = page.get("properties", {})

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
    creds_dict = json.loads(GCP_JSON, strict=False)
    scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
    gc = gspread.authorize(creds)

    sh = gc.open(SHEET_NAME)
    ws = sh.worksheet("Tareas")

    tasks = get_notion_tasks()

    ws.clear()
    ws.append_row(["Casa", "Tarea", "Estado", "Fecha_limite", "Responsable"])
    for row in tasks:
        ws.append_row(row)

    print(f"Sincronizadas {len(tasks)} tarea(s) desde Notion hacia el Sheet.")


if __name__ == "__main__":
    main()
