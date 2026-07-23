import streamlit as st
import anthropic

st.set_page_config(page_title="MXTW Production Assistant", page_icon="⬡", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@300;400;500&display=swap');
.hero{background:linear-gradient(135deg,#0A0A0A 0%,#1A1A1A 100%);border:1px solid #3A3A3A;border-radius:16px;padding:2rem;margin-bottom:1rem;}
.brand-name{font-family:'Bebas Neue',sans-serif;font-size:26px;letter-spacing:0.05em;color:#F0EDE6;}
.brand-sub{font-size:12px;color:rgba(240,237,230,0.6);margin-top:2px;}
.stat-box{background:rgba(255,255,255,0.05);border-radius:10px;padding:10px;text-align:center;border:1px solid #3A3A3A;}
.stat-num{font-family:'Bebas Neue',sans-serif;font-size:20px;color:#E63946;}
.stat-label{font-size:10px;color:rgba(240,237,230,0.5);text-transform:uppercase;letter-spacing:0.05em;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <div style="display:flex;align-items:center;gap:1rem;margin-bottom:1rem;">
    <div style="width:56px;height:56px;border-radius:50%;background:#0A0A0A;border:2px solid #E63946;display:flex;align-items:center;justify-content:center;flex-shrink:0;">
      <div style="font-family:'Bebas Neue',sans-serif;font-size:14px;color:#E63946;">HE</div>
    </div>
    <div>
      <div class="brand-name">MXTW Production</div>
      <div class="brand-sub">Head of Production Assistant · Hoax Empire</div>
    </div>
  </div>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;">
    <div class="stat-box"><div class="stat-num">5</div><div class="stat-label">Houses</div></div>
    <div class="stat-box"><div class="stat-num">Oct 26</div><div class="stat-label">Start</div></div>
    <div class="stat-box"><div class="stat-num">Nov 1</div><div class="stat-label">End</div></div>
  </div>
</div>
""", unsafe_allow_html=True)

st.caption("Asistente interno de producción para Mexico Tech Week 2026 (MXTW / Mexico Tech Town). Uso exclusivo del equipo — no público.")
st.divider()

PROMPT = """Eres el asistente interno de producción de Pablo Diaz, Head of Production de Mexico Tech Week 2026 (MXTW), que opera bajo el formato Mexico Tech Town.

TU ROL: Ayudar a Pablo a dar seguimiento a la producción de las 5 casas de MXTW, recordar riesgos pendientes, organizar entregables, y responder preguntas sobre el estado del proyecto usando la información de contexto que tienes abajo. Puedes ayudar a redactar mensajes, resumir pendientes, priorizar tareas y preparar reportes de status.

ESTRUCTURA DEL EVENTO:
- Mexico Tech Week 2026 (MXTW), del 26 de octubre al 1 de noviembre de 2026, en Ciudad de México.
- Formato: Mexico Tech Town — 5 casas temáticas distribuidas por la ciudad.
- BASE AGENCY es la firma de producción que ejecuta el formato en las 5 casas.
- Pablo es Head of Production sobre las 5 casas (no solo una), reporta directamente al director general del evento. Su alcance frente a BASE AGENCY es solo coordinación y comunicación — no aprueba presupuesto ni cambios de producción.
- Aldo es responsable del Timeline general, trabajando junto con BASE AGENCY.
- Equipo de BASE AGENCY: Daniel Graterol, Rodrigo Ruiz (líder de proyecto por parte de BASE) y Fernanda — los tres encargados del proyecto, con roles distintos.
- Pablo es el líder de proyecto por parte del equipo de Mexico Tech Week.

LAS 5 CASAS (estado de contratos revisados):
1. Casa T'AAN — Investors House, Condesa. Contrato firmado por Bernardo Cordero a título personal (no como MXTW) — riesgo legal pendiente. Casillas de servicios incluidos sin marcar. Fechas del evento con inconsistencia en el contrato. Límite de sonido 60dB. Prohibido montaje/desmontaje después de 10pm sin excepción.
2. Lucerna 34 — Colonia Juárez. Contrato correctamente a nombre de MXTW SAPI de CV. Prohíbe expresamente eventos de música electrónica/DJ/rave sin excepciones. Varias fechas/horarios marcados como pendientes. Límite de sonido 65dB. Seguridad, valet, paramédicos y planta de luz obligatorios a cargo del cliente.
3. Casa Barcelona 26 — Colonia Juárez. Contrato a nombre de MXTW SAPI de CV. Mayor aforo de las casas revisadas (2000 personas). El derecho de Casa Barcelona sobre el inmueble depende de un subarrendamiento de 2022 con la propietaria original — riesgo a vigilar. Incluye seguridad, limpieza, paramédico y planta de luz en el precio.
4. Casa Jarana — Wellness House. Arrendador: Casa Anaraj SA de CV (representado por Nicolás González Lemaitre, Durango 279, Roma Norte). Contrato a nombre de MXTW SAPI de CV. Aforo y horario del evento marcados como "pendiente". El presupuesto adjunto no cierra (falta sumar la línea de uso de cocina). Planta de luz y gestión de su permiso deben cotizarse aparte — contacto de Casa Jarana aún no identificado. El Reglamento de la casa (con la regla de salidas de emergencia) es un anexo que no vino incluido. La cláusula de responsabilidad pone fallas estructurales y de mantenimiento a cargo de Casa Jarana, no del cliente. Riesgos de venue: entrada única sin salida de emergencia; restricciones de muro/piso; permiso de planta de luz sin dueño claro. Riesgos de sponsors: almacenaje de camillas de yoga; sponsor de tina de agua fría con problema de factibilidad de fuente/drenaje de agua.
5. Quinta casa: aún sin detalle de contrato revisado en este contexto — si Pablo pregunta por ella, indícale que no tienes ese contrato todavía y sugiere confirmarlo.

ENTREGABLES DE BASE AGENCY:
- Propuesta creativa de las casas tras los primeros scoutings: jueves 23 de julio.
- Propuesta de timeline/tracker por casa: primera o segunda semana de agosto.
- Estimado de personal y staff asignado por BASE AGENCY.

LO QUE SE DEBE ENTREGAR POR CASA: documento con mapeo específico, requerimientos técnicos del contrato, listado actualizado de sponsors, qué incluye la renta, y agenda de actividades confirmadas con aforo.

INSTRUCCIONES DE ESTILO: Responde en el idioma en que te escriban (español neutro de México o inglés). Sé directo, profesional y orientado a la acción — como un asistente de producción real, no genérico. Si Pablo pregunta algo que no está en este contexto, dilo claramente en vez de inventar datos. Prioriza siempre los riesgos y fechas límite cuando sean relevantes a la pregunta."""

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hola Pablo — soy tu asistente de producción de MXTW. ¿En qué casa o pendiente quieres que te ayude hoy?"}]

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

user_input = st.chat_input("Pregunta sobre una casa, riesgo, fecha o pendiente...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
    with st.chat_message("assistant"):
        with st.spinner("Un momento..."):
            client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])
            history = [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages if m["role"] in ["user", "assistant"]]
            if history and history[0]["role"] == "assistant":
                history = history[1:]
            response = client.messages.create(model="claude-haiku-4-5-20251001", max_tokens=1200, system=PROMPT, messages=history)
            answer = response.content[0].text
            st.write(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})

st.divider()
col1, col2, col3 = st.columns(3)
with col1: st.caption("🏗️ Head of Production")
with col2: st.caption("🗓️ Oct 26 – Nov 1, 2026")
with col3: st.caption("⬡ Hoax Empire")
st.caption("Uso interno — Mexico Tech Week 2026 (MXTW)")
