import streamlit as st
from email.message import EmailMessage
import ssl
import smtplib


st.set_page_config(page_title="Cupones de Cumpleaños", page_icon="🎟️", layout="wide")

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
    
def send_email_dar(subject, body):
  
    sender_email = "samuelsuescarios@gmail.com"
    receiver_email = "djsuescar@eafit.edu.co"


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


# Configuración de la página
st.set_page_config(page_title="Cupones de Cumpleaños", page_icon="🎟️", layout="wide")

# Título con animación
st.markdown("""
    <h1 class="animate-title" style='text-align: center; font-size: 3em;'>
        🎟️ Cupones Especiales 🎟️
    </h1>
    <style>
    .animate-title {
        background-image: linear-gradient(
            -225deg,
            #FF1361 0%,
            #44107A 29%,
            #FF1361 67%,
            #FFF800 100%
        );
        background-size: auto auto;
        background-clip: border-box;
        background-size: 200% auto;
        color: #fff;
        background-clip: text;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: textclip 2s linear infinite;
    }
    @keyframes textclip {
        to {
            background-position: 200% center;
        }
    }
    </style>
""", unsafe_allow_html=True)

st.write("""
<div style='text-align: center; font-size: 1.2em; margin-bottom: 20px;'>
    🎁 ¡Aquí tienes algunos cupones especiales que puedes canjear en cualquier momento del año!<br>
    Ojo, te recomiendo no tocar el botón si no quieres canjear tu cupón.
</div>
""", unsafe_allow_html=True)

cupones = {
    "Llego tu mouskiherramienta misteriosa": "Tienes la oportunidad de esclavisarme con algo que necesites de tu elección, sin pero ni costo alguno",
    "UR MOVIE PARTNER": "Una noche de películas con tus películas favoritas (prometo no dormirme), cuando necesites compañía y no quieras hablar de los problemas, simplemente entretenerte",
    "Unas hamburguesitas o que?": "Comer hamburguesas bien chimbas, yo invito",
    "Tu arlequin de confianza": "Me puedes poner a hacer el ridículo, whenever u want",
}

# Función para crear un efecto de cupón
def cupon_effect(title, description, key):
    st.markdown(f"""
        <div style="
            background: linear-gradient(45deg, #FF9A8B 0%, #FF6A88 55%, #FF99AC 100%);
            border-radius: 15px;
            padding: 20px;
            margin: 10px 0;
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        ">
            <h3 style="color: #fff; text-align: center;">{title}</h3>
            <p style="color: #fff; text-align: center;">{description}</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button(f"🎟️ Canjear {title}", key=key):
        subject = f"Cupón canjeado: {title}"
        message = f"Tu hermana ha canjeado el cupón: {title}\nDescripción: {description}"
        message2 = f"Has canjeado el cupón de regalo de tu hermanito hermoso: {title}\nDescripción: {description}"
        if send_email(subject, message) and send_email_dar(subject, message2):
            st.balloons()
            st.success(f"¡El cupón '{title}' ha sido canjeado! Nos llegará una notificación por correo que me avisará que canjeaste el cupón.")
        else:
            st.error("Hubo un problema al canjear el cupón. Por favor, intenta de nuevo más tarde.")

# Mostrar cupones
for i, (cupon, descripcion) in enumerate(cupones.items()):
    cupon_effect(cupon, descripcion, f"cupon_{i}")

# Cupón sorpresa
st.markdown("---")
st.subheader("🎭 Cupón Sorpresa")
if st.button("Revelar Cupón Sorpresa"):
    cupones_sorpresa = [
        "Un día de spa juntos",
        "Cocinarte tu plato favorito",
        "Un día de aventura sorpresa",
        "Un concierto de tu artista favorito (si está en la ciudad)",
        "Un día de compras, yo pago"
    ]
    cupon_sorpresa = random.choice(cupones_sorpresa)
    st.markdown(f"""
        <div style="
            background: linear-gradient(45deg, #A9C9FF 0%, #FFBBEC 100%);
            border-radius: 15px;
            padding: 20px;
            margin: 10px 0;
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
            text-align: center;
            color: #fff;
        ">
            <h3>🎉 ¡Sorpresa!</h3>
            <p>{cupon_sorpresa}</p>
        </div>
    """, unsafe_allow_html=True)

# Nota final
st.markdown("""
<div style='text-align: center; font-size: 1.2em; margin-top: 20px;'>
    Estos cupones son una pequeña muestra de cuánto te quiero, hermanita.<br>
    ¡Espero que los disfrutes tanto como yo disfruto de tu compañía!<br>
    <strong>¡Feliz cumpleaños! 🎂🎉</strong>
</div>
""", unsafe_allow_html=True)