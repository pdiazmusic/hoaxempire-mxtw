import streamlit as st
import anthropic

st.set_page_config(page_title="100% Natural Pet", page_icon="🐾")

st.markdown("<style>.header{background:#1a6b3a;padding:1.5rem;border-radius:12px;margin-bottom:1.5rem;}</style>", unsafe_allow_html=True)
st.markdown("<div class='header'><div style='font-size:22px;font-weight:600;color:white;'>🐾 100% Natural Pet</div><div style='font-size:13px;color:#a8d5b5;'>Comida fresca para tu mascota</div></div>", unsafe_allow_html=True)

col1,col2,col3,col4,col5 = st.columns(5)
with col1: st.markdown("🥚 Huevo")
with col2: st.markdown("🍗 Pollo")
with col3: st.markdown("🐟 Sardina")
with col4: st.markdown("🐠 Atun")
with col5: st.markdown("🥩 Res")
st.caption("Todos con verduras y arroz")
st.divider()

PROMPT = "Eres el asistente de 100% Natural Pet en CDMX. Menu: Huevo, Pollo, Sardina, Atun o Res con verduras y arroz. Ingredientes: Papa, zanahoria, calabaza, chayote, espinaca, avena, arroz, aceite vegetal, calcio y Vitamin PET. Fresca diariamente, cero preservativos. Detecta idioma y responde en ese idioma. Si piden precio di que un asesor les contactara. Si quieren pedir pide nombre y colonia. Se amable y profesional."

if "messages" not in st.session_state:
    st.session_state.messages = [{"role":"assistant","content":"Hola! Bienvenido a 100% Natural Pet. En que te puedo ayudar?"}]

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

user_input = st.chat_input("Escribe tu pregunta / Type your question...")

if user_input:
    st.session_state.messages.append({"role":"user","content":user_input})
    with st.chat_message("user"):
        st.write(user_input)
    with st.chat_message("assistant"):
        with st.spinner("Un momento..."):
            client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])
            history = [{"role":m["role"],"content":m["content"]} for m in st.session_state.messages if m["role"] in ["user","assistant"]]
            if history and history[0]["role"] == "assistant":
                history = history[1:]
            response = client.messages.create(model="claude-haiku-4-5-20251001",max_tokens=1000,system=PROMPT,messages=history)
            answer = response.content[0].text
            st.write(answer)
    st.session_state.messages.append({"role":"assistant","content":answer})

st.divider()
st.caption("🐾 100% Natural Pet - Ciudad de Mexico")
