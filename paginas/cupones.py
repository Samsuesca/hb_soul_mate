import streamlit as st

st.title("Cupones 🎟️")

st.write("🎁 ¡Aquí tienes algunos cupones especiales que puedes canjear!")

cupones = {
    "Llego tu mouskiherramienta misteriosa": "Tienes la oportunidad de esclavisarme con algo que necesites de tu eleccion, sin pero ni costo alguno",
    "UR MOVIE PARTNER": "Una noche de películas con tus películas favoritas, cuando necesites compañia y no quieras hablar de los problemas, simplemente entrenerte",
    "Unas hamburguesitas o que?": "Comer hamburguesas bien chimbas, yo invito",
    "Tu arlequin de confianza":"Me puedes poner a hacer el ridiculo, whenever u want",
}

for cupon, descripcion in cupones.items():
    st.subheader(cupon)
    st.write(descripcion)
    st.button(f"Canjear {cupon}")
