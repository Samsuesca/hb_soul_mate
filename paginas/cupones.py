import streamlit as st
from email.message import EmailMessage
import ssl
import smtplib

def send_email(subject, body):
  

   
    sender_email = "samuelsuescarios@gmail.com"
    receiver_email = "assuescar@eafit.edu.co"


    smtp_password = "qvnx etyp erwy txmq"

    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.set_content(body)


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
