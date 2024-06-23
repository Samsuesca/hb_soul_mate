import streamlit as st
from st_pages import Page, show_pages, add_page_title,Section

st.set_page_config(page_title='Cumpleaños de la Soul Mate',
                    page_icon=':book:',
                    layout='wide')

pages = [
    Section('Menú de Tareas'),
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
nombre = "ÁNGEL SAMUEL SUESCA RIOS"
correo = "assuescar@eafit.edu.co"
id = "1000125660"
github_url = "https://github.com/Samsuesca/TAREAS-1"

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
st.title(f'Bienvenido, a la página de tareas de {nombre} para su curso de Tópicos en Econometría!')

# Información personalizada
col1,col2 = st.columns(2)
with col1:
    st.write(f'Correo: {correo}')
with col2:
    st.write(f'ID: {id}')

# Enlace al directorio de GitHub con estilo de botón
# Def una clase CSS para el botón
css = """
<style>
.custom-btn {
    background-color: #FF2733; /* Cambia el color de fondo a tu preferencia */
    color: black; /* Cambia el color del texto a tu preferencia */
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




st.write('- Puedes navegar semana tras semana para ver las tareas propuestas.')
st.write('- Si la tarea tiene ejercicios de simulación no olvides visualizar el código en el expander.')
st.write('- La gran parte de este proyecto fue basado en el libro de Microeconometría de Cameron y Trivedi. Pero también se usaron fuentes auxiliares como wikipedia, y otros post de econometria. Para las simulaciones se utilizó apoyo de las documentaciones oficiales de las librerías y softwares utilizados')






def main():
    st.title('¡Feliz Cumpleaños!')
    
    st.write('¡Bienvenida a tu página especial de cumpleaños!')
    st.write('Aquí encontrarás sorpresas y regalos especialmente para ti.')
    
    st.header('🎁 Regalo Especial')
    st.write('Para comenzar, aquí tienes un regalo muy especial:')
    st.image('images/grafica.png', caption='Tu regalo')
    
    st.header('🎉 Sección de Cupones')
    st.write('¡Descubre todos los cupones que tenemos para ti!')
    st.write('1. Cupón de Spa: Válido por una sesión de spa relajante.')
    st.write('2. Cupón de Cena: Válido por una cena gourmet en tu restaurante favorito.')
    st.write('3. Cupón de Película: Válido por una noche de películas en casa, con palomitas incluidas.')

if __name__ == '__main__':
    main()
