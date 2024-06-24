import streamlit as st
import random

# Función para centrar el contenido
def center_content(content_func, *args, **kwargs):
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        content_func(*args, **kwargs)

# Función para crear un efecto de polaroid
def polaroid_effect(image_path, caption):
    st.markdown(f"""
        <div style="
            background: white;
            padding: 10px;
            padding-bottom: 20px;
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
            width: 80%;
            margin: auto;
            transform: rotate({random.uniform(-5, 5)}deg);
        ">
            <img src="{image_path}" style="width: 100%;">
            <div style="text-align: center; padding: 10px 0;">
                <p style="font-family: 'Brush Script MT', cursive; font-size: 1.2em;">{caption}</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Título con animación
st.markdown("""
    <h1 class="animate-title" style='text-align: center; font-size: 3em;'>
        📸 Memories 📸
    </h1>
    <style>
    .animate-title {
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
    }
    @keyframes textclip {
        to {
            background-position: 200% center;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Introducción
st.write("""
<div style='text-align: center; font-size: 1.2em; margin-bottom: 20px;'>
    ¡Feliz cumpleaños, Dar! 🎉🎂<br>
    Aquí tienes un pequeño espacio dedicado a algunos recuerdos y carteles que encontré por ahí.
</div>
""", unsafe_allow_html=True)

st.write("--------")

# Sección: INEM
st.write("""
### 🏫 Cuando nos estábamos matriculando en el INEM.
No sé si recuerdas esta foto, pero yo sí. Ese día estábamos matriculándonos en el INEM. Es estupendo saber que pude empezar y terminar esa experiencia contigo, creo que ese día nos cambió la vida.
Nuevamente gracias, por dejarme seguir algunos de tus caminos.
""")

polaroid_effect("images/inem.jpeg", "El comienzo de una gran etapa")

st.write("--------")

# Sección: Parada juvenil
st.write("""
### 🎉 Cuando se te estallaron los sparkies después de la parada juvenil
Parce, recuerdo que esa madrugada me reí infinitamente de tu pendejada, no entiendo qué te pasó pero sencillamente no estabas cuerda jajajajaj.
Me meo de solo recordarlo.
""")

center_content(st.write, "<div style='text-align: center; font-style: italic;'>Mi hermana, la loca 😜</div>", unsafe_allow_html=True)
center_content(st.video, "images/laloca.mp4")

st.write("--------")

# Sección: Grados
st.write("""
### 🎓 En tus grados.
Finalizaste tu etapa en el INEM, y yo estuve ahí. Igualmente también estuviste por ahí cuando culminé mi proceso. Lo más lindo de eso es que seguimos estudiando en la misma U y vamos a tener el mismo alma mater (HASTA VIMOS UNA MATERIA JUNTOS JAJAJAJAJAJAJA).
""")

polaroid_effect("images/grados.jpeg", "Juntos Shempre")

st.write("--------")

# Sección: 2020
st.write("""
### 🎊 Empezando el 2020
Recuerdo esta sección de fotos, aunque me llames pendejo sé que me amas jajajajaja. Nos tomamos unas buenas fotos antes de que empezara la pandemia, recuerdo mucho que fueron épocas re-bonitas y permitió que cuando empezó la pandemia estuviéramos muy unidos.
""")

center_content(st.write, "<div style='text-align: center; font-style: italic;'>Nosotros loleando 😂</div>", unsafe_allow_html=True)
center_content(st.video, "images/pandemia.mp4")


# Mensaje final
st.write("""
<div style='text-align: center; font-size: 1.2em; margin-top: 20px;'>
    Dar, estos son solo algunos de los muchos recuerdos que hemos compartido.<br>
    Cada uno de ellos es especial y forma parte de nuestra historia juntos.<br>
    ¡Que sigamos creando más memorias increíbles!<br>
    <br>
    <strong>¡Feliz cumpleaños, hermanita! 🎉🎂💖</strong>
</div>
""", unsafe_allow_html=True)