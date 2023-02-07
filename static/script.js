function login() {
    let formData = new FormData(document.forms.loginform);

  // добавить к пересылке ещё пару ключ - значение
    console.log(formData);
  // отослать
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:5000/sign_in");
    xhr.onreadystatechange = function() {
        if (this.readyState != 4) return;
        if (this.responseText != 'true') {
            document.getElementById('result').innerHTML = this.responseText;
        }
        else {
            window.location.href = '/';
        }
    }
    xhr.send(formData);
}
function register() {
    let formData = new FormData(document.forms.loginform);

  // добавить к пересылке ещё пару ключ - значение
    console.log(formData);
  // отослать
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:5000/sign_up");
    xhr.onreadystatechange = function() {
        if (this.readyState != 4) return;
        if (this.responseText != 'true') {
            document.getElementById('result').innerHTML = this.responseText;
        }
        else {
            window.location.href = '/';
        }
    }
    xhr.send(formData);
}