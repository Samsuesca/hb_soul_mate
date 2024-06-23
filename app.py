import streamlit as st
from st_pages import Page, show_pages, add_page_title, Section

st.set_page_config(page_title='Cumpleaños de la Soul Mate',
                   page_icon=':birthday:',
                   layout='wide')

pages = [
    Section('Menú de Cumpleaños'),
    Page("app.py", "🏠 Inicio"),
    Page("paginas/soul_mate.py", "SOUL MATE", "1️⃣ "),
    Page("paginas/cupones.py", "CUPONES", "2️⃣ "),
    Page("paginas/celia.py", "CELIA", "3️⃣ ")
]

# Muestra las páginas en la barra lateral
show_pages(pages)

# Inicializa la estructura de páginas
add_page_title()
# Variables globales
nombre = "Darcita"
correo = "correo@example.com"
id = "1000123456"
github_url = "https://github.com/TuUsuario/TuRepositorio"

# Personalizar el estilo de la página
st.markdown(
    """
    <style>
    .centered {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    .btn-link {
        background-color: #007BFF;
        color: white;
        border-radius: 5px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        padding: 10px 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Título de la página
st.title(f'¡Bienvenida, {nombre}, a tu página de cumpleaños! 🎉')


st.write('- ¡Disfruta navegando por tus secciones especiales en esta página de cumpleaños!')
st.write('- ¡Cada sección tiene una sorpresa para ti!')

