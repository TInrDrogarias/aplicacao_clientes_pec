function login(){
	let login = document.getElementById("input_box1").value;
	let senha = document.getElementById("input_box2").value;

	if (login == "admin" && senha == "admin") {
		alert('sucesso');
		location.href = "app.html"
	} else {
		alert('usuario n encontrado')
	}
}