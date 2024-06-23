import streamlit as st

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
