
let request_in_progress = "False" ;

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
        if (request_in_progress === "False") {
            update_user(phrase)
            request_in_progress = "True"
        }
        else {
            document.getElementById("inp").value = "Papy réfléchi encore a une réponse";
        }

    }
}

function request_ajax(data_txt) {
    $.ajax({
    url: '/request_ajax/',
    type : 'GET',
    data: {'request_user' : data_txt},
    success : function(result) {
        update_papy_text(result.address)
        update_papy_image(result.image)
        update_papy_text(result.history)
        spinner_off()
        request_in_progress = "False"
        document.getElementById("inp").value = "";
    }});/*$.ajax*/
}

function spinner_on() {

    let newDiv = document.createElement("div");
    newDiv.className = "spinner";
    newDiv.id = "spinner";
    let center = document.createElement("center");
    let newContent = document.createTextNode("/");
    center.appendChild(newContent);
    newDiv.appendChild(center);

    let currentDiv = document.getElementById('zone_button');

    currentDiv.appendChild(newDiv);
}
function spinner_off(){
    let spinnerDiv = document.getElementById('spinner');
    let zone_buttonDiv = document.getElementById('zone_button');
    zone_buttonDiv.removeChild(spinnerDiv);
}

function update_user(text) {
    spinner_on()
    request_ajax(text);
    let newDiv = document.createElement("div");
    newDiv.className = "user";
    let newContent = document.createTextNode(text);
    newDiv.appendChild(newContent);

    let currentDiv = document.getElementById('tchat');
    currentDiv.appendChild(newDiv);
    currentDiv.scrollTop += 100;
}

function update_papy_text(text) {
    let newDiv = document.createElement("div");
    newDiv.className = "computer";
    let newContent = document.createTextNode(text);
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
