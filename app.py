import streamlit as st
import anthropic

st.set_page_config(page_title="100% Natural Pet", page_icon="🐾", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600&family=DM+Sans:wght@300;400;500&display=swap');
.hero{background:linear-gradient(135deg,#0d4a27 0%,#1a6b3a 60%,#2d8a50 100%);border-radius:16px;padding:2rem;margin-bottom:1rem;}
.brand-name{font-family:'Playfair Display',serif;font-size:22px;font-weight:600;color:white;}
.stat-box{background:rgba(255,255,255,0.12);border-radius:10px;padding:10px;text-align:center;border:1px solid rgba(255,255,255,0.15);}
.stat-num{font-family:'Playfair Display',serif;font-size:22px;font-weight:600;color:white;}
.stat-label{font-size:10px;color:rgba(255,255,255,0.65);}
.price-featured{background:#e8f5ee;border:1.5px solid #1a6b3a;border-radius:12px;padding:12px;text-align:center;}
.price-regular{background:#f8f8f8;border-radius:12px;padding:12px;text-align:center;}
.price-amount{font-family:'Playfair Display',serif;font-size:24px;font-weight:600;color:#0d4a27;}
.best-badge{background:#1a6b3a;color:white;font-size:9px;padding:2px 8px;border-radius:10px;display:inline-block;margin-bottom:4px;}
.ingredient-tag{background:#e8f5ee;color:#0d4a27;font-size:12px;padding:4px 12px;border-radius:20px;display:inline-block;margin:2px;}
.benefit-box{background:#f8f8f8;border-radius:10px;padding:10px 12px;margin-bottom:8px;}
.step-num{background:#1a6b3a;color:white;width:24px;height:24px;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:11px;font-weight:500;margin-right:8px;}
.zone-tag{background:#f0f0f0;border-radius:20px;padding:4px 12px;font-size:12px;display:inline-block;margin:2px;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <div style="display:flex;align-items:center;gap:1rem;margin-bottom:1rem;">
    <div style="width:56px;height:56px;border-radius:50%;background:white;display:flex;align-items:center;justify-content:center;flex-shrink:0;border:2px solid rgba(255,255,255,0.3);">
      <div style="font-family:serif;font-size:9px;font-weight:bold;color:#0d4a27;text-align:center;line-height:1.3;">100%<br>NATURAL<br>PET</div>
    </div>
    <div>
      <div class="brand-name">100% Natural Pet</div>
      <div style="font-size:12px;color:rgba(255,255,255,0.7);margin-top:2px;">Nutrición real para mascotas reales</div>
    </div>
  </div>
  <div style="display:flex;gap:6px;flex-wrap:wrap;margin-bottom:1rem;">
    <span style="background:rgba(255,255,255,0.15);color:white;font-size:11px;padding:4px 10px;border-radius:20px;border:1px solid rgba(255,255,255,0.2);">📍 Ciudad de México</span>
    <span style="background:rgba(255,255,255,0.15);color:white;font-size:11px;padding:4px 10px;border-radius:20px;border:1px solid rgba(255,255,255,0.2);">✓ Sin preservativos</span>
    <span style="background:rgba(255,255,255,0.15);color:white;font-size:11px;padding:4px 10px;border-radius:20px;border:1px solid rgba(255,255,255,0.2);">🌿 100% natural</span>
  </div>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;">
    <div class="stat-box"><div class="stat-num">200+</div><div class="stat-label">mascotas felices</div></div>
    <div class="stat-box"><div class="stat-num">2</div><div class="stat-label">años de experiencia</div></div>
    <div class="stat-box"><div class="stat-num">6</div><div class="stat-label">alcaldías CDMX</div></div>
  </div>
</div>
""", unsafe_allow_html=True)

st.subheader("🍽️ Nuestro menú")
col1,col2,col3,col4,col5 = st.columns(5)
with col1: st.markdown("🥚\n\n**Huevo**\n\ncon verduras")
with col2: st.markdown("🍗\n\n**Pollo**\n\ncon verduras")
with col3: st.markdown("🐟\n\n**Sardina**\n\ncon verduras")
with col4: st.markdown("🐠\n\n**Atún**\n\ncon verduras")
with col5: st.markdown("🥩\n\n**Res**\n\ncon verduras")
st.caption("Todos incluyen: arroz + verduras de temporada + Vitamin PET + calcio")
st.divider()

st.subheader("📏 Porciones por tamaño")
col1,col2,col3 = st.columns(3)
with col1: st.info("🐕 **Raza pequeña**\nhasta 10 kg\n\n**150g** por porción")
with col2: st.info("🐕‍🦺 **Raza mediana**\n10 — 25 kg\n\n**300g** por porción")
with col3: st.info("🦮 **Raza grande**\nmás de 25 kg\n\n**500g** por porción")
st.divider()

st.subheader("💰 Planes y precios")
col1,col2,col3 = st.columns(3)
with col1:
    st.markdown('<div class="price-regular"><div style="font-size:11px;color:gray;">Porción individual</div><div class="price-amount">$45</div><div style="font-size:10px;color:gray;">MXN por pieza</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="price-featured"><div class="best-badge">más popular</div><div style="font-size:11px;color:#0d4a27;">Paquete semanal</div><div class="price-amount">$280</div><div style="font-size:10px;color:#1a6b3a;">7 porciones · ahorras $35</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="price-regular"><div style="font-size:11px;color:gray;">Paquete quincenal</div><div class="price-amount">$520</div><div style="font-size:10px;color:gray;">14 porciones · ahorras $110</div></div>', unsafe_allow_html=True)
st.success("🚚 Envío gratis en pedidos mayores a $300 MXN · Pedido mínimo $200 MXN")
st.divider()

tab1,tab2,tab3,tab4 = st.tabs(["✨ Beneficios","🌿 Ingredientes","📦 Cómo pedir","📍 Zonas"])

with tab1:
    col1,col2 = st.columns(2)
    with col1:
        st.markdown("**✨ Pelaje brillante**\nMejora visible en 2 a 4 semanas")
        st.markdown("**⚡ Más energía**\nNutrición real y completa")
    with col2:
        st.markdown("**💚 Mejor digestión**\nReduce gases y malestares")
        st.markdown("**🛡️ Sin aditivos**\nCero conservadores artificiales")

with tab2:
    st.markdown("""
    <div>
    <span class="ingredient-tag">🥔 Papa</span>
    <span class="ingredient-tag">🥕 Zanahoria</span>
    <span class="ingredient-tag">🎃 Calabaza</span>
    <span class="ingredient-tag">🌿 Chayote</span>
    <span class="ingredient-tag">🍃 Espinaca</span>
    <span class="ingredient-tag">🌾 Avena</span>
    <span class="ingredient-tag">🍚 Arroz</span>
    <span class="ingredient-tag">🫙 Aceite vegetal</span>
    <span class="ingredient-tag">💊 Calcio</span>
    <span class="ingredient-tag">⭐ Vitamin PET</span>
    </div>
    """, unsafe_allow_html=True)
    st.caption("Preparada fresca cada mañana. Cocida al vapor para preservar nutrientes.")

with tab3:
    for i,step in enumerate(["Escríbenos por WhatsApp o por este chat","Dinos tu nombre, colonia y tamaño de tu mascota","Elige tu proteína favorita y el plan que prefieras","Confirmamos y te damos hora de entrega","Recibes tu comida fresca en la puerta de tu casa"],1):
        st.markdown(f"**{i}.** {step}")
    st.caption("Pedidos con mínimo 24 horas de anticipación. Pago por transferencia, efectivo o en línea.")

with tab4:
    st.markdown("""
    <div>
    <span class="zone-tag">📍 Benito Juárez</span>
    <span class="zone-tag">📍 Coyoacán</span>
    <span class="zone-tag">📍 Tlalpan</span>
    <span class="zone-tag">📍 Iztapalapa</span>
    <span class="zone-tag">📍 Miguel Hidalgo</span>
    <span class="zone-tag">📍 Cuauhtémoc</span>
    </div>
    """, unsafe_allow_html=True)
    col1,col2 = st.columns(2)
    with col1:
        st.markdown("**Atención:** Lunes a sábado\n\n**Horario:** 8:00am — 7:00pm")
    with col2:
        st.markdown("**Entregas:** 9:00am — 6:00pm\n\n**Anticipación:** 24 horas mínimo")

st.divider()

phone = "525611274706"
wa_link = f"https://wa.me/{phone}?text=Hola,%20me%20interesa%20pedir%20comida%20natural%20para%20mi%20mascota."
st.markdown(f'<a href="{wa_link}" target="_blank" style="display:block;background:#25D366;color:white;text-align:center;padding:14px;border-radius:12px;font-weight:500;text-decoration:none;margin-bottom:1rem;font-size:15px;">📱 Pedir por WhatsApp</a>', unsafe_allow_html=True)

PROMPT = "Eres el asistente virtual de 100% Natural Pet, empresa de comida natural para mascotas en Ciudad de Mexico. HISTORIA: Fundados por amor a los perros. Nuestra mascota Lola tenia problemas digestivos con croquetas. Llevamos 2 anos alimentando a mas de 200 mascotas en CDMX. MENU: Huevo, Pollo, Sardina, Atun o Res con verduras y arroz. INGREDIENTES: Papa, zanahoria, calabaza, chayote, espinaca, avena, arroz, aceite vegetal, calcio y Vitamin PET. BENEFICIOS: Mejora pelaje en 2-4 semanas, reduce problemas digestivos, mas energia, sin conservadores. PORCIONES: Pequena hasta 10kg 150g, mediana 10-25kg 300g, grande mas 25kg 500g. PRECIOS: Individual $45 MXN, semanal 7 porciones $280 MXN, quincenal 14 porciones $520 MXN, envio gratis pedidos mayores $300 MXN, minimo $200 MXN. COMO PEDIR: WhatsApp o chat, dar nombre colonia y tamano mascota, elegir proteina y plan. ZONAS: Benito Juarez, Coyoacan, Tlalpan, Iztapalapa, Miguel Hidalgo, Cuauhtemoc. HORARIOS: Lunes a sabado, 8am-7pm, entregas 9am-6pm, pedidos con 24hrs anticipacion. CONTACTO: WhatsApp 5611274706, Instagram @naturalpet.cdmx. INSTRUCCIONES: Detecta idioma y responde en ese idioma, espanol natural de Mexico o ingles, pide nombre colonia y tamano si quieren pedir, se amable y profesional."

if "messages" not in st.session_state:
    st.session_state.messages = [{"role":"assistant","content":"Hola! Bienvenido a 100% Natural Pet 🐾 Somos tu opcion de comida fresca y natural en CDMX. En que te puedo ayudar hoy?"}]

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
col1,col2,col3 = st.columns(3)
with col1: st.caption("📱 @naturalpet.cdmx")
with col2: st.caption("🕐 Lun-Sab 8am-7pm")
with col3: st.caption("📍 6 alcaldías CDMX")
st.caption("🐾 100% Natural Pet — Sin preservativos · Preparado diario · Con Vitamin PET · +200 mascotas felices")