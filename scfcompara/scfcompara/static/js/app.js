const boton_subir = document.querySelector("#boton_subir");
const boton_limpiar = document.querySelector("#boton_limpiar");

boton_limpiar.addEventListener('click', ()=>{
    console.log('click')
})

const vel_puerto1 = document.querySelector(".vel_puerto1");
const vel_puerto2 = document.querySelector(".vel_puerto2");

function Comparar(dato1,dato2){
    if (dato1.innerHTML === "" & dato2.innerHTML === ""){
        dato1.className = ''
        dato2.className = '' 
    }else if(dato1.innerHTML === dato2.innerHTML){
        dato1.classList.add('bg-success')
        dato2.classList.add('bg-success') 
        console.log(dato1)
        console.log(dato2)       
    }else{
        dato1.classList.add('bg-danger')
        dato2.classListadd('bg-danger')
    }
}

Comparar(vel_puerto1,vel_puerto2)



/* if (vel_puerto1.innerHTML === '' & vel_puerto2.innerHTML === ''){
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
} */
