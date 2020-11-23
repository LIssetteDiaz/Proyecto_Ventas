
class Carrito{
    comprarProducto(e){
        e.preventDefault();
        if(e.target.classList.contains('agregar-carrito')){
            const producto = e.target.parentElement.parentElement;
            this.leerDatosProducto(producto);
        }
    }

    leerDatosProducto(producto){
        let valor;
        if(producto.querySelector('#numero').value >= 1){
            valor = producto.querySelector('#numero').value;
        }
        else{
            valor = 1; 
        }
        
        const infoProducto = {
            imagen : producto.querySelector('img').src,
            titulo : producto.querySelector('h4').textContent,
            precio : producto.querySelector('strong').textContent,
            id : producto.querySelector('a').getAttribute('data-id'),
            cantidad : valor
        }
        let productosLS;
        productosLS = this.obtenerProductosLocalStorage();
        productosLS.forEach(function(productoLS){
            if(productoLS.id === infoProducto.id){
                productosLS = productoLS.id;
            }
        });
        if(productosLS === infoProducto.id){
            Swal.fire({
                type: 'info',
                title: 'Oops...',
                text: 'El producto ya esta agregado',
                timer: 2000,
                showConfirmButton: false
            })
        }
        else{
            this.insertarCarrito(infoProducto);
        }
        
    }

    insertarCarrito(producto){
        const row = document.createElement('tr');
        row.innerHTML = `
            <td><img src="${producto.imagen}" width=100></td>
            <td>${producto.titulo}</td>
            <td>${producto.precio}</td>
            <td>
                ${producto.cantidad}
            </td>
            <td><i class="borrar-producto fas fa-trash-alt btn btn-outline-danger"  data-id="${producto.id}"></i></td>
        `;
        listaProductos.appendChild(row);
        this.guardarProductosLocalStorage(producto);
    }

    eliminarProducto(e){
        e.preventDefault();
        let producto, productoID;
        if(e.target.classList.contains('borrar-producto')){
            e.target.parentElement.parentElement.remove();
            producto = e.target.parentElement.parentElement;
            productoID = producto.querySelector('i').getAttribute('data-id');
        }
        this.eliminarProductoLocalStorage(productoID);
    }

    vaciarCarrito(e){
        e.preventDefault();
        while(listaProductos.firstChild){
            listaProductos.removeChild(listaProductos.firstChild);
        }
        this.vaciarLocalStorage();
        return false;
    }

    guardarProductosLocalStorage(producto){
        let productos;
        productos = this.obtenerProductosLocalStorage();
        productos.push(producto);
        localStorage.setItem('productos', JSON.stringify(productos));
    }

    obtenerProductosLocalStorage(){
        let productoLS;

        if(localStorage.getItem('productos') === null){
            productoLS = [];
        }
        else{
            productoLS = JSON.parse(localStorage.getItem('productos'));
        }
        return productoLS;
    }

    eliminarProductoLocalStorage(productoID){
        let productosLS;
        productosLS = this.obtenerProductosLocalStorage();
        productosLS.forEach(function(productoLS, index){
            if(productoLS.id === productoID){
                productosLS.splice(index, 1);
            }
        });

        localStorage.setItem('productos', JSON.stringify(productosLS));
    }

    leerLocalStorage(){
        let productosLS;
        productosLS = this.obtenerProductosLocalStorage();
        productosLS.forEach(function(producto){
            const row = document.createElement('tr');
            row.innerHTML = `
                <td><img src="${producto.imagen}" width=100></td>
                <td>${producto.titulo}</td>
                <td>${producto.precio}</td>
                <td>
                    ${producto.cantidad}
                </td>
                <td><i class="borrar-producto fas fa-trash-alt btn btn-outline-danger" data-id="${producto.id}"></i></td>
            `;
            listaProductos.appendChild(row);
        });
    }
        
    leerLocalStorageComprar(){
        let productosLS;
        productosLS = this.obtenerProductosLocalStorage();
        productosLS.forEach(function(producto){
            const row = document.createElement('tr');
            row.innerHTML = `
                <td><img src="${producto.imagen}" width=60></td>
                <td>${producto.titulo}</td>
                <td>$${producto.precio}</td>
                <td>
                    ${producto.cantidad}
                </td>
            `;
            listaCompra.appendChild(row);
        });
    }

    vaciarLocalStorage(){
        localStorage.clear();
    }

    procesarPedido(e){
        e.preventDefault();
        if(this.obtenerProductosLocalStorage().length === 0){
            Swal.fire({
                type: 'error',
                title: 'Oops...',
                text: 'El carrito esta vacio',
                timer: 2000,
                showConfirmButton: false
            })
        }
        else{
            location.href = "compra";
        }
        
    }

    calcularTotal(){
        let productoLS;
        let total = 0;
        let totalDolar = 0;
        productoLS = this.obtenerProductosLocalStorage();
        console.log(productoLS);
        for(let i = 0; i < productoLS.length; i++){
           
            let num1 = Number(productoLS[i].precio);
            let num2 = Number(productoLS[i].cantidad);

            let element = (num1 * num2);
            total = total + element;
            function roundTo(value, places){
                var power = Math.pow(10, places);
                return Math.round(value * power) / power;
            }
            totalDolar = roundTo(total / 764.20, 2);
            // totalDolar = totalDolar.toString().replace(/\./g,',');
        }
        document.getElementById('total').innerHTML = total.toLocaleString();
        document.getElementById('dolar').innerHTML = totalDolar.toLocaleString('en-US');
    }
    // http://127.0.0.1:8000/venta/compra/index.html
}