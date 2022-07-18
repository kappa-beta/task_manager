let tasks_task_create = '/tasks/';

formElem.onsubmit = async (e) => {
	e.preventDefault();

	let test = new FormData(formElem)

	var object = {};
		test.forEach(function(value, key){
		object[key] = value;
	});
	var json = JSON.stringify(object);
	console.log(json);

	let response = await fetch(tasks_task_create, {
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