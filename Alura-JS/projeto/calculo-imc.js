// peso / altura * altura

var peso = 100
var altura = 2.0

if (altura != 0){
	var imc = peso / (altura * altura)

	console.log(imc)
}else{
	console.log("Altura igual a zero")
}