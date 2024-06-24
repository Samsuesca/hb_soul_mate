import streamlit as st

st.title("Soul Mate 💖")

# Introducción
st.write("""
¡Feliz cumpleaños, my Soul Mate!
Aquí tienes un pequeño espacio dedicado a ti para recordarte lo especial que eres.
""")

# Función para centrar el contenido
def center_content(content_func, *args, **kwargs):
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        content_func(*args, **kwargs)

# Primera imagen y audio
center_content(st.image, "images/i0.png", caption="¡Feliz Cumpleaños!")
center_content(st.audio, "audios/a1.mpeg", format='audio/mpeg')

st.write("--------")

# Texto intercalado
st.write("""
### Por ser quien creció conmigo y me acompañó en tantos momentos.
Hermanita, siempre recordaré tu compañía desde el día cero. Vivimos momentos mágicos que nunca olvidaré y que hoy recuerdo de la manera más bella posible.
Desde las veces en las que jugábamos a que éramos adultos, que teníamos trabajos y que nos invitábamos a nuestros apartamentos (pd: me encanta que la vida nos haya permitido que ya me invites al tuyo jejejee).
O cuando cantábamos imaginándonos que éramos una banda de rock con Pipe y la dábamos toda definitivamente. 
Es imposible que recuerde todos esos bellos momentos, pero imaginar mi infancia es bonito porque disfruté al lado de alguien increíble como tú.
""")

center_content(st.video, "videos/v2.mp4")
st.write("Juntos desde chititos")

st.write("--------")

# Texto intercalado
st.write("""
### My guide.
Muchas veces fuiste mi guía. A veces reflexiono y concluyo que lo más probable es que hubiera sido un raro que nunca explotó sus habilidades sociales si no me hubieras
cogido e invitado a tus proyectos. Definitivamente agradezco tanto por hacerme crecer y seguir algunos de tus caminos. En muchos aspectos soy quien soy, gracias a ti.
""")

# Imágenes intercaladas
center_content(st.image, "images/onu.jpeg", caption="Cuando me ayudaste a crecer, antes de crecer")
center_content(st.image, "images/med.jpeg", caption="En el proceso mi fai")
center_content(st.image, "images/guapos.jpeg", caption="Ahora sí, guapos y poderosos")

st.write("--------")

# Texto intercalado
st.write("""
### Mi compañía.
Dar, definitivamente te agradezco por ser mi compañera de muchos momentos y la hermanita que siempre estuvo ahí para mí. Me encanta tener una hermanita que brille como yo, o que incluso brille mucho más.
En realidad, nos vemos geniales como hermanos y fuera de charla, aunque fuiste recogida en un basurero, agradezco el día en que la cucha le dio por hacer semejante acto de caridad.
JAJAJAJAJA, mentiras, por nada del mundo te cambiaría o negaría a un ser tan espectacular como tú.
""")

center_content(st.video, "videos/v3.mp4")
st.write("Y faltan muchos más momentos juntos por vivir")

st.write("--------")

# Texto de cierre
st.write("""
My soul mate.
Herma, tú misma lo has dicho, tú y yo tenemos una conexión especial. Tal vez sea algo como el ying y el yang o cualquiera de esas mondades, le podemos poner el misticismo que sea, pero la realidad es esa.
Nosotros, dentro de nuestro entorno, nuestra familia, y dentro de este extraño universo tenemos una relación especial y que destaca, somos seres radiantes individualmente y juntos. De alguna manera siento que estamos destinados a cosas muy, pero muy grandes, tanto individualmente como juntos.
Siento que llegarás infinitamente lejos hermanita, tanto como lo siento para mí.
""")

# Imagen de cierre
center_content(st.image, "images/tuyyohoy.png", caption="Te Amo 💖")

st.write("""
Mi hermana, llegaremos lejos,
Eres alguien demasiado radiante y una estrella que en sus fases de vida cada vez brilla más.
""")
