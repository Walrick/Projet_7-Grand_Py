
//Ne fonctionne pas, a revoir
function pressEnter(event) {
    let code = event.keyCode;
    if (code==13) { //le code de la touche Enter
        check_text()
    }
}

function check_text() {
    let phrase = document.getElementById("inp").value;
    if (phrase != "" & phrase != " ") {
        document.getElementById("inp").value = "";
        update_user(phrase)
    }
}

function request_ajax(data_txt) {
    $.ajax({
    url: '/test_ajax/',
    type : 'GET',
    data: {'variable' : data_txt},
    success : function(result) {
        update_papy_text(result.status)
        update_papy_image(result.image)
    }});/*$.ajax*/
}

function update_user(text) {
    request_ajax(text);
    let newDiv = document.createElement("div");
    newDiv.className = "user";
    newContent = document.createTextNode(text);
    newDiv.appendChild(newContent);

    let currentDiv = document.getElementById('tchat');
    currentDiv.appendChild(newDiv);
    currentDiv.scrollTop += 100;
}

function update_papy_text(text) {
    let newDiv = document.createElement("div");
    newDiv.className = "computer";
    newContent = document.createTextNode(text);
    newDiv.appendChild(newContent);

    let currentDiv = document.getElementById('tchat');
    currentDiv.appendChild(newDiv);
    currentDiv.scrollTop += 100;
}

function update_papy_image(image) {
    let newDiv = document.createElement("div");
    newDiv.className = "computer";
    let newImg = document.createElement("img");
    newImg.src = image
    newDiv.appendChild(newImg);

    let currentDiv = document.getElementById('tchat');
    currentDiv.appendChild(newDiv);
    currentDiv.scrollTop += 300;
}
