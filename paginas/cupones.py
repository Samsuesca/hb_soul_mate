import streamlit as st
from email.message import EmailMessage
import ssl
import smtplib
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configuración del servidor SMTP
smtp_server = os.getenv("SMTP_SERVER")
smtp_port = os.getenv("SMTP_PORT")
sender_email = os.getenv("SMTP_USER")
smtp_password = os.getenv("SMTP_PASSWORD")
receiver_email = os.getenv("TO_EMAIL")
# = "samuelsuescarios@gmail.com"
#= "assuescar@eafit.edu.co"

def send_email(subject, message):
  

   
    body = "Este es un correo de prueba enviado desde un script de Python."

    #smtp_server = "smtp.gmail.com"
    #smtp_port = 587
    #smtp_username = "samuelsuescarios@gmail.com"
    smtp_password = "qvnx etyp erwy txmq"

    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.set_content(message)


    context = ssl.create_default_context()


    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(sender_email,smtp_password) 
        smtp.sendmail(sender_email,receiver_email,message.as_string())


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
        if send_email(subject, message):
            st.success(f"¡El cupón '{cupon}' ha sido canjeado! Te llegará una notificación por correo.")
        else:
            st.error(f"No se pudo canjear el cupón '{cupon}'. Intenta nuevamente.")
