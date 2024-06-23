import streamlit as st
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configuración del servidor SMTP
smtp_server = os.getenv("SMTP_SERVER")
smtp_port = os.getenv("SMTP_PORT")
smtp_user = os.getenv("SMTP_USER")
smtp_password = os.getenv("SMTP_PASSWORD")
to_email = os.getenv("TO_EMAIL")

def send_email(subject, message, to_email):
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = smtp_user
    msg["To"] = to_email

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()  # Identificar con el servidor
        server.starttls()  # Iniciar TLS para la seguridad
        server.ehlo()  # Volver a identificar una vez que TLS esté activo
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, to_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        st.error(f"Error al enviar el correo: {e}")
        return False

st.title("Cupones 🎟️")

st.write("🎁 ¡Aquí tienes algunos cupones especiales que puedes canjear!")

cupones = {
    "Llego tu mouskiherramienta misteriosa": "Tienes la oportunidad de esclavisarme con algo que necesites de tu eleccion, sin pero ni costo alguno",
    "UR MOVIE PARTNER": "Una noche de películas con tus películas favoritas, cuando necesites compañia y no quieras hablar de los problemas, simplemente entrenerte",
    "Unas hamburguesitas o que?": "Comer hamburguesas bien chimbas, yo invito",
    "Tu arlequin de confianza":"Me puedes poner a hacer el ridiculo, whenever u want",
}

for cupon, descripcion in cupones.items():
    st.subheader(cupon)
    st.write(descripcion)
    if st.button(f"Canjear {cupon}"):
        subject = f"Cupón canjeado: {cupon}"
        message = f"Tu hermana ha canjeado el cupón: {cupon}\nDescripción: {descripcion}"
        if send_email(subject, message, to_email):
            st.success(f"¡El cupón '{cupon}' ha sido canjeado! Te llegará una notificación por correo.")
        else:
            st.error(f"No se pudo canjear el cupón '{cupon}'. Intenta nuevamente.")
