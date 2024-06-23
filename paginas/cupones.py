import streamlit as st

st.title("Cupones 🎟️")

st.write("🎁 ¡Aquí tienes algunos cupones especiales que puedes canjear!")

cupones = {
    "Desayuno en la cama": "Un desayuno especial preparado por mí.",
    "Noche de películas": "Una noche de películas con tus películas favoritas.",
    "Día de spa": "Un día de relajación con masajes y tratamientos faciales."
}

for cupon, descripcion in cupones.items():
    st.subheader(cupon)
    st.write(descripcion)
    st.button(f"Canjear {cupon}")
