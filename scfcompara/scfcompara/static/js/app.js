const boton_subir = document.querySelector("#boton_subir");
const boton_limpiar = document.querySelector("#boton_limpiar");

boton_limpiar.addEventListener('click', ()=>{
    console.log('click')
})

const vel_puerto1 = document.querySelector(".vel_puerto1");
const vel_puerto2 = document.querySelector(".vel_puerto2");
console.log(vel_puerto1);
console.log(vel_puerto2)

if (vel_puerto1.innerHTML === '' & vel_puerto2.innerHTML === ''){
    vel_puerto1.className = 'vel_puerto1';
    vel_puerto2.className = 'vel_puerto2';

}else if (vel_puerto1.innerHTML === vel_puerto2.innerHTML){
    vel_puerto1.classList.add('bg-success')
    vel_puerto2.classList.add('bg-success')
    console.log(vel_puerto1)
    console.log(vel_puerto2)
}
else{
    vel_puerto1.classList.add('bg-danger')
    vel_puerto2.classList.add('bg-danger')
}
