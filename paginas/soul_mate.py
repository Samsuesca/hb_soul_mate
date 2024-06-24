import streamlit as st
import random
## se debe actualizar ahora
# Función para centrar el contenido
def center_content(content_func, *args, **kwargs):
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        content_func(*args, **kwargs)

# Función para crear un efecto de confeti
def confetti():
    st.markdown(
        """
        <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
        <script>
        confetti({
            particleCount: 100,
            spread: 70,
            origin: { y: 0.6 }
        });
        </script>
        """,
        unsafe_allow_html=True,
    )

# Configuración de la página
st.set_page_config(page_title="Soul Mate 💖", page_icon="💖", layout="wide")

# Título con animación
st.markdown("""
    <h1 class="animate-character" style='text-align: center; font-size: 3em;'>
        Soul Mate 💖
    </h1>
    <style>
    .animate-character {
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
    ¡Feliz cumpleaños, my Soul Mate! 🎉🎂<br>
    Aquí tienes un pequeño espacio dedicado a ti para recordarte lo especial que eres.
</div>
""", unsafe_allow_html=True)

# Activar confeti
confetti()

# Primera imagen y audio
center_content(st.image, "images/i0.png", caption="¡Feliz Cumpleaños!")
center_content(st.audio, "audios/a1.mpeg", format='audio/mpeg')

st.write("--------")

# Sección: Creciendo juntos
st.write("""
### 👫 Por ser quien creció conmigo y me acompañó en tantos momentos.
Hermanita, siempre recordaré tu compañía desde el día cero. Vivimos momentos mágicos que nunca olvidaré y que hoy recuerdo de la manera más bella posible.

- 🏠 Las veces en que jugábamos a ser adultos, con trabajos y apartamentos (¡me encanta que ahora me invites al tuyo de verdad, pronto te invitaré al mio!).
- 🎸 Cuando formábamos nuestra banda de rock con Pipe y lo dábamos todo. Menos mal no somos cantantes ahora jajajaja
- 💖 Cada recuerdo de nuestra infancia es especial porque lo compartí contigo, a pesar de que cuando niños peleabamos, hoy valoro increiblemente tenerte como hermana.

Esos momentos son tesoros que guardaré siempre en mi corazón.
""")

center_content(st.video, "videos/v2.mp4")
center_content(st.write, "<div style='text-align: center; font-style: italic;'>Juntos desde chititos 👶👧</div>", unsafe_allow_html=True)

st.write("--------")

# Sección: Mi guía
st.write("""
### 🧭 My guide.
Muchas veces fuiste mi guía, y te lo agradezco infinitamente:

- 🌱 Me ayudaste a desarrollar mis habilidades sociales. Gracias a ti creci como amigo y como hombre, aunque no lo creas
- 🚀 Me invitaste a participar en tus proyectos, impulsándome a crecer. Conoci personas, lugares y vivi momentos increibles porque me tuviste en cuenta.
- 🌟 Gran parte de quien soy hoy es gracias a tu influencia positiva en mi vida.

Tu apoyo y ejemplo han sido fundamentales en mi desarrollo personal.
""")

# Galería de imágenes
col1, col2, col3 = st.columns(3)
with col1:
    st.image("images/onu.jpeg", caption="Cuando me ayudaste a crecer, antes de crecer")
with col2:
    st.write("Si así hemos crecido en tan poco tiempo, que nos detendrá en un futuro?")
    st.image("images/med.jpeg", caption="En el proceso mi fai")
    st.write("Seguro nada, sis")
with col3:
    st.image("images/guapos.jpeg", caption="Ahora sí, guapos y poderosos")

st.write("--------")

# Sección: Mi compañía
st.write("""
### 👯‍♀️ Mi compañía.
Dar, eres la compañera perfecta en cada etapa de mi vida:

- 💪 Siempre estás ahí para mí, en los buenos y malos momentos.
- ✨ Tu brillo me inspira a ser mejor cada día, y el ver que sobresales tanto me invita a hacer lo mismo.
- 😂 Nuestro sentido del humor compartido hace que cada momento sea especial y que sin importar que, pueda reirme contigo.

Aunque bromee sobre que fuiste "recogida en un basurero", la verdad es que eres un regalo demasiado valioso para mi. Agradezco a la cucha por pasar por el basurero.
""")

center_content(st.video, "videos/v3.mp4")
center_content(st.write, "<div style='text-align: center; font-style: italic;'>Y faltan muchos más momentos juntos por vivir 🚀</div>", unsafe_allow_html=True)

st.write("--------")

# Sección: Soul Mate
st.write("""
### 🔮 My soul mate.
Herma, nuestra conexión es única y especial:

- ☯️ No se si somos como el yin y el yang, complementarios y en perfecto equilibrio, le podemos meter el mistisismo que sea.
- 🌠 El hecho es que individualmente brillamos, pero juntos somos brutales sis.
- 🚀 Estamos destinados a cosas grandes, tanto por separado como juntos. Y eso es hermoso

Siento que llegarás infinitamente lejos, hermanita, tanto como lo siento para mí. Tu potencial es ilimitado.
""")

# Imagen de cierre
center_content(st.image, "images/tuyyohoy.jpeg", caption="Te Amo 💖")

# Mensaje final
st.write("""
<div style='text-align: center; font-size: 1.2em; margin-top: 20px;'>
    Mi hermana, llegaras muy lejos,<br>
    Eres una estrella que brilla cada vez más intensamente.<br>
    Gracias por ser mi soul mate, mi consejera y confidente.<br>
    Que cumplas mil años más y el universo siga disfrutando de ti.<br>
    <br>
    <strong>¡Feliz cumpleaños, mi querida Soul Mate! 🎉🎂💖</strong>
</div>
""", unsafe_allow_html=True)

