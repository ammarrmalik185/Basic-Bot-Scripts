var prices = document.getElementsByClassName("td__price")
var conversionRatio = 219.55;
var taxAmmount = 13;


// for new element
function Process(elem){
    var number = Number.parseFloat(elem.textContent.split("$")[1]);
    var elem2 = document.createElement("h3");
    elem2.style = "font-size: medium;";
    elem.appendChild(elem2);
    elem2.textContent = "Rs " + (Math.round((number * conversionRatio * (1+taxAmmount/100)) * 100) / 100).toLocaleString("en-PK");
}

for (let name of prices) {
    Process(name);
}

function Process(elem){
    var number = Number.parseFloat(elem.textContent.split("$")[1]);
    var elem2 = document.createElement("h3");
    elem2.style = "font-size: medium;";
    elem.parentElement.insertBefore(elem2, elem);
    elem2.textContent = "Rs " + (Math.round((number * conversionRatio * (1+taxAmmount/100)) * 100) / 100).toLocaleString("en-PK");
}

function Process(elem){
    var number = Number.parseFloat(elem.textContent.split("$")[1]);
    elem.textContent = "Rs " + (Math.round((number * conversionRatio * (1+taxAmmount/100)) * 100) / 100).toLocaleString("en-PK");
}