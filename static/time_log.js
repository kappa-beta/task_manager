function sendJSON() {
    let a = window.location.href.substring(window.location.href.lastIndexOf('/') + 1);
    let tasks_task_edit = '/tasks/'+a+'/time_log';
    let xhr = new XMLHttpRequest();
    let url = tasks_task_edit;
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
        result.innerHTML = this.responseText;
      }
    };
    var d = new Date();
    var data = JSON.stringify({ "start": d.toLocaleDateString('en-ca')});
    xhr.send(data);
}

function sendJSON_end() {
    let a = window.location.href.substring(window.location.href.lastIndexOf('/') + 1);
    let tasks_task_edit = '/tasks/'+a+'/time_log';
    let xhr = new XMLHttpRequest();
    let url = tasks_task_edit;
    xhr.open("PATCH", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
        result.innerHTML = this.responseText;
      }
    };
    var d = new Date();
    var data = JSON.stringify({ "end": d.toLocaleDateString('en-ca')});
    xhr.send(data);
}