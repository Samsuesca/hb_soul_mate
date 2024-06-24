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

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(sender_email,smtp_password) 
            smtp.sendmail(sender_email,receiver_email,message.as_string())
        return True
    except smtplib.SMTPException as e:
        st.error(f"Error al enviar el correo: {e}")
        return False

st.title("Cupones 🎟️")

st.write("🎁 ¡Aquí tienes algunos cupones especiales que puedes canjear en cualquier momento del año!")
st.write("Ojo, te recomiendo no tocar el botón si no quieres canjear tu cupon")

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
        send_email(subject, message)
        st.success(f"¡El cupón '{cupon}' ha sido canjeado! Me llegará una notificación por correo que me avisará que canjeaste el cupon.")
     