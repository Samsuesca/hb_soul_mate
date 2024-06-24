import streamlit as st

st.title("📸 Memories 📸")

# Introducción
st.write("""
¡Feliz cumpleaños, Dar!
Aquí tienes un pequeño espacio dedicado a algunos recuerdos y carteles que encontré por ahī.
""")


st.write("--------")

# Texto intercalado
st.write("""
### Cuando nos estabamos matriculando en el INEM.
No sé si recuerdes esta foto, pero yo si. Ese dia estabamos matriculandonos en el INEM. Es estupendo saber que pude empezar y terminar esa experiencia contigo, creo que ese dia nos cambio la vida.
Nuevamente gracias, por dejarme seguir algunos de tus caminos
""")

st.images("images/inem.jpeg", caption= "El comienzo de una gran etapa")
# Segunda imagen

st.write("--------")

# Texto intercalado
st.write("""
### Cuando se te estallaron los sparkies despues de la parada juvenil
Parce, recuerdo que esa madrugada me rei infinitamente de tu pendejada, no entiendo que te pasó pero sencillamente no estabas cuerda jajajajaj.
Me meo de solo recordarlo
""")

# Tercera imagen
st.video("images/laloca.mp4",format="video/mp4", subtitles="Mi hermana, la loca")

st.write("--------")

# Texto de cierre
st.write("""
En tus grados. 
Finalizaste tu etapa en el INEM, y yo estuve ahí. Igualmente también estuviste por ahí cuando culmine mi proceso. Lo más lindo de eso es que seguimos estudiando en la misma U y vamos a tener el mismo alma mater (HASTA VIMOS UNA MATERIA JUNTOS JAJAJAJAJJAJJAJA)
""")

# Imagen de cierre
st.image("images/grados.jpeg", caption="Juntos Shempre")


st.write("--------")

# Texto intercalado
st.write("""
### Empezando el 2020
Recuerdo esta sección de fotos, aunque me llames pendejo se que me amas jajajajaja. Nos tomamos unas buenas fotos antes de que empezará la pandemia, recuerdo mucho que fueron épocas re-bonitas y permitió que cuando empezó la pandemia estuvieramos muy unidos
""")

# Cuarta imagen
st.video("images/pandemia.mp4",format="video/mp4", subtitles="Nosotros loleando")


