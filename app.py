import streamlit as st
import anthropic

st.set_page_config(page_title="100% Natural Pet", page_icon="🐾", layout="centered")

st.markdown('<style>.header{background:#1a6b3a;padding:1.5rem 2rem;border-radius:12px;margin-bottom:1.5rem;display:flex;align-items:center;gap:1.5rem;}</style>', unsafe_allow_html=True)

st.markdown("""
<div class="header">
    <div style="width:64px;height:64px;border-radius:50%;background:white;display:flex;align-items:center;justify-content:center;font-size:10px;font-weight:bold;color:#1a6b3a;text-align:center;line-height:1.2;border:3px solid #a8d5b5;padding:8px;flex-shrink:0;">100%<br>NATURAL<br>PET</div>
    <div>
        <div style="font-size:22px;font-weight:600;color:white;">100% Natural Pet</div>
        <div style="font-size:13px;color:#a8d5b5;margin-top:4px;">Comida fresca para tu mascota / Fresh food for your pet</div>
        <span style="background:#a8d5b5;color:#0d4a27;font-size:11px;padding:3px 10px;border-radius:20px;margin-top:6px;display:inline-block;">Ciudad de México</span>
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)
with col1: st.markdown("🥚 **Huevo**")
with col2: st.markdown("🍗 **Pollo**")
with col3: st.markdown("🐟 **Sardina**")
with col4: st.markdown("🐠 **Atún**")
with col5: st.markdown("🥩 **Res**")
st.caption("Todos con verduras y arroz / All with vegetables and rice")
st.divider()

phone = "525611274706"
wa_link = f"https://wa.me/{phone}?text=Hola,%20me%20interesa%20pedir%20comida%20natural%20para%20mi%20mascota."
st.markdown(f'<a href="{wa_link}" target="_blank" style="display:block;background:#25D366;color:white;text-align:center;padding:12px;border-radius:8px;font-weight:bold;text-decoration:none;margin-bottom:1rem;">📱 Pedir por WhatsApp / Order via WhatsApp</a>', unsafe_allow_html=True)

SYSTEM_PROMPT = "Eres el asistente virtual de 100% Natural Pet, empresa de comida natural para mascotas en Ciudad de Mexico. MENU: Huevo, Pollo, Sardina, Atun o Carne de Res con verduras y arroz. INGREDIENTES: Papa, zanahoria, calabaza, chayote, espinaca, avena, arroz, aceite vegetal, calcio y Vitamin PET. DIFERENCIAL: Preparada fresca diariamente, cero preservativos, cero aditivos. INSTRUCCIONES: Detecta el idioma y responde en ese mismo idioma. Espanol natural de Mexico o ingles. Si preguntan precio di que un asesor les contactara. Si quieren pedir solicita nombre y colonia. Se amable, calido y profesional siempre."

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hola! Bienvenido a 100% Natural Pet. En que te puedo ayudar hoy?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Escribe tu pregunta / Type your question...")

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
            response = client.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=1000,
                system=SYSTEM_PROMPT,
                messages=history
            )
            answer = response.content[0].text
            st.write(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})

st.divider()
st.caption("🐾 100% Natural Pet — Ciudad de México | Sin preservativos · Preparado diario · Con Vitamin PET")
