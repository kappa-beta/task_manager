let login = '/auth/login/';

formElem.onsubmit = async (e) => {
	e.preventDefault();

	let test = new FormData(formElem)

	var object = {};
		test.forEach(function(value, key){
		object[key] = value;
	});
	var json = JSON.stringify(object);
	console.log(json);

	let response = await fetch(login, {
	method: 'POST',
		headers: {
			'Accept': 'application/json',
			'Content-Type': 'application/json'
		},
		body: json
	});

	let result = await response.json();
	console.log(result);
};