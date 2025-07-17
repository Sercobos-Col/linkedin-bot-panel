import streamlit as st, os
from linkedin_bot import run_bot

st.set_page_config(page_title="Bot LinkedIn - Sercobos", layout="centered")
st.title("🤖 Bot Automático de LinkedIn")
st.subheader("Aplicador Global – Powered by Sergio Cobos")

email = st.text_input("Correo LinkedIn", value=os.getenv("LINKEDIN_USERNAME"))
password = st.text_input("Contraseña", type="password", value=os.getenv("LINKEDIN_PASSWORD"))
keywords = st.text_input("Palabras clave", value="Ingeniero Civil, Oil & Gas, Jefe de Producción")
ubicacion = st.text_input("Ubicación", value="Global")

if st.button("🚀 Iniciar Bot"):
    if email and password:
        st.success("Bot en marcha, aplicando ofertas...")
        run_bot(email, password, keywords, ubicacion)
        st.balloons()
    else:
        st.error("Completa tus credenciales")
