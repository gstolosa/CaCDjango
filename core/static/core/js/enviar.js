const form = document.getElementById("form")
const button = document.getElementById("submitButton")


const nombre = document.getElementById("nombre")
const apellido = document.getElementById("apellido")
const nacimiento = document.getElementById("nacimiento")
const celular = document.getElementById("celular")
const email = document.getElementById("email")
const mensaje = document.getElementById("mensaje")

const formValido = {
    nombre: false,
    apellido: false,
    nacimiento: false,
    celular: false,
    email: false,
    mensaje: false,

}

form.addEventListener ("submitButton", (e) => {
    e.preventDefault();
    validarForm()
})

nombre.addEventListener("change", (e) => {
    if(e.target.value.trim().length > 0) formValido.nombre = true
})

apellido.addEventListener("change", (e) => {
    if(e.target.value.trim().length > 0) formValido.apellido = true
})

nacimiento.addEventListener("change", (e) => {
    if(e.target.value.trim().length > 0) formValido.nacimiento = true
})

celular.addEventListener("change", (e) => {
    if(e.target.value.trim().length > 0) formValido.celular = true
})

email.addEventListener("change", (e) => {
    if(e.target.value.trim().length > 0) formValido.email = true
})

mensaje.addEventListener("change", (e) => {
    if(e.target.value.trim().length > 0) formValido.mensaje = true
})

const validarForm = () =>{
    const formValues = Object.values(formValido)
    const valido = formValues.findIndex(value => value == false)
    if(valido == -1) form.submitButton()
    else alert("formulario invalido")
    
}