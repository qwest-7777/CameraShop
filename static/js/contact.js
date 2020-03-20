

const errors = (numbers , inputId , spanId) => {
    let inputValue = document.getElementById('input-' + inputId).value;
    if(inputValue ===""){
        document.getElementById('' + spanId).style.display = "unset";
        document.getElementById('' + spanId).innerText = "Необходимо заполнить " + '"' + numbers + '"';
        document.getElementById('input-' + inputId).style.boxShadow = "0 0 10px rgba(255, 0, 0, 0.2)";
        document.getElementById('input-' + inputId).style.borderColor = "red";
    } else {
        document.getElementById('' + spanId).style.display = "none";
        document.getElementById('' + spanId).innerText = "";
        document.getElementById('input-' + inputId).style.boxShadow = "0 0 10px rgba(0, 0, 0, 0.16)";
        document.getElementById('input-' + inputId).style.borderColor = "#CCCCCC";
    }
};