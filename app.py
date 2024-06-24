import streamlit as st
from st_pages import Page, show_pages, add_page_title
import base64

st.set_page_config(page_title='Cumpleaños de la Soul Mate', page_icon='🎂', layout='wide')

pages = [
    Page("app.py", "🏠 Inicio"),
    Page("paginas/soul_mate.py", "💖 SOUL MATE"),
    Page("paginas/cupones.py", "🎟️ CUPONES"),
    Page("paginas/celia.py", "📸 MEMORIES")
]

# Muestra las páginas en la barra lateral
show_pages(pages)

# Inicializa la estructura de páginas
add_page_title()

# Variables globales
nombre = "Darcita"
github_url = "https://github.com/TuUsuario/TuRepositorio"

# Función para convertir una imagen a base64
def get_image_as_base64(file):
    with open(file, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Personalizar el estilo de la página
st.markdown(
    """
    <style>
    .stApp {
        background-image: linear-gradient(to right top, #d16ba5, #c777b9, #ba83ca, #aa8fd8, #9a9ae1, #8aa7ec, #79b3f4, #69bff8, #52cffe, #41dfff, #46eefa, #5ffbf1);
        background-attachment: fixed;
    }
    .centered {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    .btn-link {
        background-color: #FF69B4;
        color: white;
        border-radius: 25px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 18px;
        margin: 10px 5px;
        cursor: pointer;
        padding: 12px 24px;
        transition: all 0.3s ease;
    }
    .btn-link:hover {
        background-color: #FF1493;
        transform: scale(1.05);
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: rgba(255, 255, 255, 0.1);
        color: white;
        text-align: center;
        padding: 10px 0;
        font-style: italic;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Título de la página con animación
st.markdown(
    f"""
    <h1 class="animate-character" style='text-align: center; font-size: 3em;'>
        ¡Feliz Cumpleaños, {nombre}! 🎉
    </h1>
    <style>
    .animate-character {{
        background-image: linear-gradient(
            -225deg,
            #231557 0%,
            #44107a 29%,
            #ff1361 67%,
            #fff800 100%
        );
        background-size: auto auto;
        background-clip: border-box;
        background-size: 200% auto;
        color: #fff;
        background-clip: text;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: textclip 2s linear infinite;
    }}
    @keyframes textclip {{
        to {{
            background-position: 200% center;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Mostrar video
st.write("Dar, cuando pequeña.")
st.video("videos/v1.mp4", start_time=7)

# Mensaje de bienvenida
st.markdown(
    f"""
    <div style='background-color: rgba(255,255,255,0.1); padding: 20px; border-radius: 10px; margin-top: 20px;'>
        <h2 style='color: #FF1493;'>¡Hola {nombre}! 👋</h2>
        <p style='font-size: 18px; color: #333;'>
        Este es un regalo especial para ti en tu cumpleaños, creado por tu hermano nerd con mucho amor. He diseñado esta página web para celebrar tu día de una manera única y especial, dándole un toque mío jeje. Aquí encontrarás diferentes secciones, cada una con una sorpresa diseñada especialmente para ti.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

##comentarios para commit
# Secciones de la página
st.markdown(
    """
    <h3 style='color: #FF1493; margin-top: 30px;'>Explora tu regalo:</h3>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <a href='#' class='btn-link'>🏠 Inicio</a>
        <p>La página de bienvenida donde estás ahora.</p>
        <a href='https://happybirthdaytomysoulmate.streamlit.app/SOUL%20MATE' class='btn-link'>💖 Soul Mate</a>
        <p>Un rincón especial dedicado a nuestra hermandad.</p>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <a href='https://happybirthdaytomysoulmate.streamlit.app/CUPONES' class='btn-link'>🎟️ Cupones</a>
        <p>Cupones canjeables por regalos y actividades.</p>
        <a href='https://happybirthdaytomysoulmate.streamlit.app/MEMORIES' class='btn-link'>📸 Memories</a>
        <p>Recuerdos especiales que quiero compartir contigo.</p>
        """,
        unsafe_allow_html=True
    )

# Mensaje final
st.markdown(
    """
    <div style='background-color: rgba(255,255,255,0.1); padding: 20px; border-radius: 10px; margin-top: 30px;'>
        <p style='font-size: 18px; color: #333; text-align: center;'>
        Espero que disfrutes navegando por estas secciones y que cada una de ellas te haga sentir lo especial que eres para mí. ¡Que tengas un cumpleaños maravilloso!
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Footer
st.markdown(
    """
    <div class='footer'>
        Creado con ❤️ por tu hermano nerd
    </div>
    """,
    unsafe_allow_html=True
)