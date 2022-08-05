let tasks_task_create = '/tasks/';
let a = window.location.href.substring(window.location.href.lastIndexOf('/') + 1);
let tasks_task_edit = '/tasks/'+a;


formElemEdit.onsubmit = async (e) => {
	e.preventDefault();

	let test = new FormData(formElemEdit)

	var object = {};
		test.forEach(function(value, key){
		object[key] = value;
	});
	var json = JSON.stringify(object);
	console.log(json);

	let response = await fetch(tasks_task_edit, {
	method: 'PATCH',
		headers: {
			'Accept': 'application/json',
			'Content-Type': 'application/json'
		},
		body: json
	});

	let result = await response.json();
	console.log(result);
	console.log(a);
};