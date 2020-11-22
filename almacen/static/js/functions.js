function mostrarTipos(numero_id){
    var1 = console.log(document.querySelectorAll("span"));
    console.log(numero_id);

    var1.array.forEach(element => {
        if (element.id == numero_id) {
            console.log("funciona");
        }
    });


    // if (var1 = numero_id){
    //     document.getElementsByTagName("span").style.display="block";
    //     // console.log("funciona");
    // }
}