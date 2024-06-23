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
nombre = "Tu Hermana"
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

# Información personalizada
col1, col2 = st.columns(2)
with col1:
    st.write(f'Correo: {correo}')
with col2:
    st.write(f'ID: {id}')

# Enlace al directorio de GitHub con estilo de botón
css = """
<style>
.custom-btn {
    background-color: #FF2733; /* Cambia el color de fondo a tu preferencia */
    color: white; /* Cambia el color del texto a tu preferencia */
    padding: 10px 20px; /* Ajusta el relleno según tus preferencias */
    border: none;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 19px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 4px; /* Ajusta el radio del borde según tus preferencias */
}
</style>
"""

# Aplica el estilo CSS
st.markdown(css, unsafe_allow_html=True)
st.write('---')
# Agrega el botón con la clase CSS personalizada
st.markdown(
    f'**Apretar el botón para ir al directorio fuente de la página:**<br>'
    f'<a class="btn-link custom-btn" href="{github_url}" target="_blank">Visitar GitHub</a>',
    unsafe_allow_html=True,
)

# Separador visual
st.write('---')

st.write('- ¡Disfruta navegando por tus secciones especiales en esta página de cumpleaños!')
st.write('- ¡Cada sección tiene una sorpresa para ti!')

