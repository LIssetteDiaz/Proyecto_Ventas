const compra = new Carrito();
const listaCompra = document.querySelector('#lista-compra tbody');
const procesarCompraBtn = document.getElementById('procesar-compra');
const cliente = document.getElementById('cliente');
const correo = document.getElementById('correo');
// const carrito = document.getElementById('carrito');

cargarEventos();

function cargarEventos(){
    document.addEventListener('DOMContentLoaded', compra.leerLocalStorageComprar());
    
    // carrito.addEventListener('click', (e)=>{compra.eliminarProducto(e)});
    compra.calcularTotal();

    procesarCompraBtn.addEventListener('click', procesarCompra);
}

function procesarCompra(e){
    e.preventDefault();
    if(cliente.value === '' || correo.value === ''){
        Swal.fire({
            type: 'error',
            title: 'Oops...',
            text: 'ingrese los campos requeridos',
            timer: 2000,
            showConfirmButton: false
        })

        // Swal.fire({
        //     type: 'error',
        //     title: 'Oops...',
        //     text: 'No hay productos seleccionados',
        //     timer: 2000,
        //     showConfirmButton: false
        // }).then(function(){
        //     window.location = "venta/";
        // })
    }
    else{
        const cargandoGif = document.querySelector('#cargando');
        cargandoGif.style.display = 'block';

        const enviado = document.createElement('img');
        enviado.src = '../../images/mail.gif';
        enviado.style.display = 'block';
        enviado.width = '150';

        setTimeout(() => {
            cargandoGif.style.display = 'none';
            document.querySelector('#loaders').appendChild(enviado);
            setTimeout(() => {
                enviado.remove();
                compra.vaciarLocalStorage();
                window.location = "../../venta/";
            }, 2000);
        }, 3000);
    }
}