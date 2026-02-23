import streamlit as st

st.set_page_config(page_title="Entradas y Botones", page_icon="🎛️")

st.markdown("# Widgets Interactivos")
st.sidebar.header("Entradas y Botones")

st.write(
    """
    La interactividad es clave en Streamlit. Los widgets son elementos de interfaz de usuario
    que permiten al usuario introducir datos.
    """
)

st.header("1. Botones")
if st.button('Púlsame'):
    st.write('¡Has pulsado el botón!')

st.divider()

st.header("2. Checkbox y Radio Buttons")
agree = st.checkbox('Estoy de acuerdo')
if agree:
    st.write('¡Genial!')

genre = st.radio(
    "¿Cuál es tu género de película favorito?",
    ('Comedia', 'Drama', 'Documental'))

if genre == 'Comedia':
    st.write('Has seleccionado: Comedia.')
else:
    st.write(f"Has seleccionado: {genre}")

st.divider()

st.header("3. Selección (Selectbox y Multiselect)")
option = st.selectbox(
    '¿Cómo te gustaría ser contactado?',
    ('Email', 'Teléfono', 'Teléfono móvil'))

st.write('Seleccionaste:', option)

options = st.multiselect(
    '¿Cuáles son tus colores favoritos?',
    ['Verde', 'Amarillo', 'Rojo', 'Azul'],
    ['Amarillo', 'Rojo'])

st.write('Seleccionaste:', options)

st.divider()

st.header("4. Sliders e Inputs")
number = st.slider('Selecciona un número', 0, 100, 50)
st.write('El número seleccionado es ', number, '🤰')

title = st.text_input('Título de la película', 'La vida es bella')
st.write('La película actual es', title)
