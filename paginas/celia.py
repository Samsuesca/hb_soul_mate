import streamlit as st

st.title("📸 Memories 📸")

# Introducción
st.write("""
¡Feliz cumpleaños, Dar!
Aquí tienes un pequeño espacio dedicado a algunos recuerdos y carteles que encontré por ahí.
""")

st.write("--------")

# Función para centrar el contenido
def center_content(content_func, *args, **kwargs):
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        content_func(*args, **kwargs)

# Texto intercalado
st.write("""
### Cuando nos estábamos matriculando en el INEM.
No sé si recuerdas esta foto, pero yo sí. Ese día estábamos matriculándonos en el INEM. Es estupendo saber que pude empezar y terminar esa experiencia contigo, creo que ese día nos cambió la vida.
Nuevamente gracias, por dejarme seguir algunos de tus caminos.
""")

center_content(st.image, "images/inem.jpeg", caption="El comienzo de una gran etapa")

st.write("--------")

# Texto intercalado
st.write("""
### Cuando se te estallaron los sparkies después de la parada juvenil
Parce, recuerdo que esa madrugada me reí infinitamente de tu pendejada, no entiendo qué te pasó pero sencillamente no estabas cuerda jajajajaj.
Me meo de solo recordarlo.
""")

center_content(st.write, "Mi hermana, la loca")
center_content(st.video, "images/laloca.mp4")

st.write("--------")

# Texto de cierre
st.write("""
En tus grados.
Finalizaste tu etapa en el INEM, y yo estuve ahí. Igualmente también estuviste por ahí cuando culminé mi proceso. Lo más lindo de eso es que seguimos estudiando en la misma U y vamos a tener el mismo alma mater (HASTA VIMOS UNA MATERIA JUNTOS JAJAJAJAJAJAJA).
""")

center_content(st.image, "images/grados.jpeg", caption="Juntos Shempre")

st.write("--------")

# Texto intercalado
st.write("""
### Empezando el 2020
Recuerdo esta sección de fotos, aunque me llames pendejo sé que me amas jajajajaja. Nos tomamos unas buenas fotos antes de que empezara la pandemia, recuerdo mucho que fueron épocas re-bonitas y permitió que cuando empezó la pandemia estuviéramos muy unidos.
""")

center_content(st.write, "Nosotros loleando")
center_content(st.video, "images/pandemia.mp4")
