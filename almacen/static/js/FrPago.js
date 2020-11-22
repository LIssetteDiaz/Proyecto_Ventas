//alert("persona")
mpPago = new FrPago();
function FrPago(){
	//alert("persona new")
	function leerLocal(){
		alert("Leyendo Local")

	}
	this.leer = function(){
		var stDatos = "proyecto_almacen=" + document.getElementById("txId").value
		var reg = ventana.getPostData("pagoLeer",stDatos)
		document.getElementById("txId").value=reg[0].fields.id;     
		document.getElementById("txDescripcion").value=reg[0].fields.descripcion;     
	

		document.getElementById("btLeer").disabled = true;
		document.getElementById("btActualizar").disabled = false;
		document.getElementById("btEliminar").disabled = false;
		document.getElementById("btCancelar").disabled = false;

        document.getElementById("txId").disabled = true;
		document.getElementById("txDescripcion").disabled = false;
			 

		/*
		alert("Leyenco Publica OK" + reg.ok)
		alert("Leyenco Publica msg" + reg.msg)
		alert("Leyenco Publica claudio" + reg.claudio)
		*/
		//leerLocal()
	}
	this.actualizar = function(){
		//alert(2)
		var stDatos = "run=" + document.getElementById("txRun").value
		       + "&nombres=" + document.getElementById("txNombres").value
		       + "&apePaterno=" + document.getElementById("txApePaterno").value		
		       + "&apeMaterno=" + document.getElementById("txApeMaterno").value		
		       + "&imagen=" + document.getElementById("txImagen").value		
		var reg = ventana.getPostData("personaActualizar",stDatos)
		if (reg.ok){
			alert(reg.msg)
			return
		}
		alert("Error ,"+ reg.msg)
		//alert("Actuaizar Publica")
	}
	this.eliminar = function(){
		var stDatos = "run=" + document.getElementById("txRun").value
		var reg = ventana.getPostData("personaDelete",stDatos)
		if (reg.ok){
			alert(reg.msg)
			return
		}
		alert("Error ,"+ reg.msg)

		//alert("eliminar Publica")
	}
	this.cancelar = function(){
		//alert("Cancelar Publica")
		document.getElementById("btLeer").disabled = false;
		document.getElementById("btActualizar").disabled = true;
		document.getElementById("btEliminar").disabled = true;
		document.getElementById("btCancelar").disabled = true;

        document.getElementById("txRun").disabled = false;
		document.getElementById("txNombres").disabled = true;
		document.getElementById("txApePaterno").disabled = true;		 
		document.getElementById("txApeMaterno").disabled = true;		 
		document.getElementById("txImagen").disabled = true;		

        document.getElementById("txRun").value = ""
		document.getElementById("txNombres").value = ""
		document.getElementById("txApePaterno").value = ""
		document.getElementById("txApeMaterno").value = ""
		document.getElementById("txImagen").value = ""


	}
				
}