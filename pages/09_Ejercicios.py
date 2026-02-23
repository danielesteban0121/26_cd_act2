import streamlit as st

st.title("Primera prueba")

title = st.text_input("¿Cuál es tu nombre?", "")

st.write(f"Hola, {title}!")if title else st.write("Por favor, ingresa tu nombre.")

st.divider()

st.header("Calcular numeros")

num1 = st.number_input("inserta un numero",value =None) 

if num1 is not None:
    if num1 > 100:
        st.warning("El número es muy grande, por favor ingresa un número menor a 100.")
        num1 = None

if num1 is not None:
    num2 = st.number_input("Ingresa otro número", value=None)
    if num2 is not None:
        resultado = st.write(f"El resultado es: {num1 + num2}")

st.divider()

st.header("Convertidor de Temperatura (Radio Buttons)")

conversion = st.radio(
    "Selecciona la conversión de temperatura:", 
    ('Celsius a Fahrenheit', 'Fahrenheit a Celsius')
)

if conversion == 'Celsius a Fahrenheit':
    celsius = st.number_input("Ingresa la temperatura en Celsius", value=None)
    if celsius is not None:
        fahrenheit = (celsius * 9/5) + 32
        st.write(f"{celsius} °C es igual a {fahrenheit} °F")
elif conversion == 'Fahrenheit a Celsius':
    fahrenheit = st.number_input("Ingresa la temperatura en Fahrenheit", value=None)
    if fahrenheit is not None:
        celsius = (fahrenheit - 32) * 5/9
        st.write(f"{fahrenheit} °F es igual a {celsius} °C")

st.divider()

st.header("Galerí­a de Mascotas (Tabs)")

tab1, tab2, tab3 = st.tabs(["Gatos", "Perros", "Aves"])

with tab1:
    st.header("Gatos")
    st.image("https://imgs.search.brave.com/xuqDIMxJM6RPJrx6XImRHdHYV89grC_sr6PKbEGQmkg/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly90NC5m/dGNkbi5uZXQvanBn/LzE4Lzc5LzAyLzUz/LzM2MF9GXzE4Nzkw/MjUzMjNfRmRxQXVW/Y1diM09DVkQ1TUha/cXRRaE5DRlVuMVlX/MUQuanBn", width=200)

with tab2:
    st.header("Perros")
    st.image("https://imgs.search.brave.com/0x9Blm4o7NPn4YUfnEPaF4LaoMSlntesvl2JF228ltc/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly90My5m/dGNkbi5uZXQvanBn/LzAwLzA2LzUxLzI0/LzM2MF9GXzY1MTI0/ODNfckZYODc5NWtX/d1pXS3Z5OWJYQk9P/OXpxdVlLd1ByTDYu/anBn", width=200)
    
with tab3:
    st.header("Aves")
    st.image("https://imgs.search.brave.com/o4-rABysrPE2smjmpP4OdLx2tKmffPm9JoALsu1sEeA/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly93d3cu/ZWplbXBsb3MuY28v/d3AtY29udGVudC91/cGxvYWRzLzIwMTcv/MDYvYXZlcy1wYWph/cm9zLWMtZTE0OTc1/MzU0NjU1NjAuanBn", width=200)

megusta = st.button("Me gusta")
if megusta:
    st.toast("Te gusta esta mascota", icon="❤️")

st.divider()

st.title(" Ejercicio 5: Caja de Comentarios (Formulario)")

with st.form("my_form"):
    st.write("Caja de Comentarios")
    
    asunto = st.text_input("Asunto")
    comentario = st.text_area("Comentario")

    submitted = st.form_submit_button("Enviar Comentario")
    
if submitted:
    st.toast("Comentario enviado con éxito!") 
    st.json({
        "asunto": asunto,
        "comentario": comentario})    
    
    
  
st.divider()

st.title("Sesion simulada")

if 'login' not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    if st.button("Ingresar"):
        if username == "admin" and password == "1234":
            st.session_state.login = True
            st.success("¡Inicio de sesión exitoso!")
        else:
            st.error("Usuario o contraseña incorrectos.")
else:
    st.write("¡Bienvenido, admin!")
    if st.button("Cerrar sesión"):
        st.session_state.login = False
        st.success("Has cerrado sesión.")
            










