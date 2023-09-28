/* const boton_subir = document.querySelector("#boton_subir");
const boton_limpiar = document.querySelector("#boton_limpiar"); */

/* boton_limpiar.addEventListener('click', ()=>{
    console.log('click')
}) */

const vel_puerto1 = document.querySelector(".vel_puerto1");
const vel_puerto2 = document.querySelector(".vel_puerto2");
const vel_puerto3 = document.querySelector(".vel_puerto3");
const vel_puerto4 = document.querySelector(".vel_puerto4");
const vel_puerto5 = document.querySelector(".vel_puerto5");
const vel_puerto6 = document.querySelector(".vel_puerto6");
const vel_puerto7 = document.querySelector(".vel_puerto7");
const vel_puerto8 = document.querySelector(".vel_puerto8");
const l2_qos1 = document.querySelector(".l2_qos1");
const l2_qos2 = document.querySelector(".l2_qos2");
const switching_enabled1 = document.querySelector(".switching_enabled1");
const switching_enabled2 = document.querySelector(".switching_enabled2");

Comparar(vel_puerto1,vel_puerto2);
Comparar(vel_puerto3,vel_puerto4);
Comparar(vel_puerto5,vel_puerto6);
Comparar(vel_puerto7,vel_puerto8);
Comparar(l2_qos1,l2_qos2);
Comparar(switching_enabled1,switching_enabled2)


 function Comparar(dato1,dato2){
     if(dato1.innerHTML === "" & dato2.innerHTML === ""){
        dato1.className = '';
        dato2.className = '';
    }else  if (dato1.innerHTML === dato2.innerHTML){
        dato1.classList.add('bg-success');
        dato2.classList.add('bg-success');
    }else{
        dato1.classList.add('bg-danger');
        dato2.classList.add('bg-danger');
    }
} 

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
