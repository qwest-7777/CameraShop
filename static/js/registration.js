

let valuePass = "";
const errors = (numbers , inputId , spanId) => {
    let inputValue = document.getElementById('' + inputId).value;
    if(numbers !== "Пароль" && numbers !== "Повтор пароля"){
        if(inputValue === ""){
            document.getElementById('error-input' + spanId).style.display = "unset";
            document.getElementById('error-input' + spanId).innerText = "Необходимо заполнить " + '"' + numbers + '"';
            document.getElementById('' + inputId).style.boxShadow = "0 0 10px rgba(255, 0, 0, 0.2)";
            document.getElementById('' + inputId).style.borderColor = "red";
        } else {
            document.getElementById('error-input' + spanId).style.display = "none";
            document.getElementById('error-input' + spanId).innerText = "";
            document.getElementById('' + inputId).style.boxShadow = "0 0 10px rgba(0, 0, 0, 0.16)";
            document.getElementById('' + inputId).style.borderColor = "#CCCCCC";

        }
    } else if(numbers === "Пароль"){
        if(inputValue === ""){
            document.getElementById('error-input' + spanId).style.display = "unset";
            document.getElementById('error-input' + spanId).innerText = "Необходимо вести" + '"' + numbers + '"';
            document.getElementById('' + inputId).style.boxShadow = "0 0 10px rgba(255, 0, 0, 0.2)";
            document.getElementById('' + inputId).style.borderColor = "red";
        } else {
            if(inputValue.length > 5){
                document.getElementById('error-input' + spanId).style.display = "none";
                document.getElementById('error-input' + spanId).innerText = "";
                document.getElementById('' + inputId).style.boxShadow = "0 0 10px rgba(0, 0, 0, 0.16)";
                document.getElementById('' + inputId).style.borderColor = "#CCCCCC";
                valuePass = document.getElementById('' + inputId).value;
                console.log(valuePass);
            } else {
                document.getElementById('error-input' + spanId).style.display = "unset";
                document.getElementById('error-input' + spanId).innerText = "Пароль должен состоять неменее 6 значение";
                document.getElementById('' + inputId).style.boxShadow = "0 0 10px rgba(255, 0, 0, 0.2)";
                document.getElementById('' + inputId).style.borderColor = "red";
            }
        }
    } else if(numbers === "Повтор пароля") {
        let valueRePass = document.getElementById('' + inputId).value;
        console.log(valueRePass);
        if(valuePass !== valueRePass){
            document.getElementById('error-input' + spanId).style.display = "unset";
            document.getElementById('error-input' + spanId).innerText = "'Несовпадает' введите пароль правильно";
            document.getElementById('' + inputId).style.boxShadow = "0 0 10px rgba(255, 0, 0, 0.2)";
            document.getElementById('' + inputId).style.borderColor = "red";
        } else {
            document.getElementById('error-input' + spanId).style.display = "none";
            document.getElementById('error-input' + spanId).innerText = "";
            document.getElementById('' + inputId).style.boxShadow = "0 0 10px rgba(0, 0, 0, 0.16)";
            document.getElementById('' + inputId).style.borderColor = "#CCCCCC";
            valuePass = document.getElementById('' + inputId).value;
        }
    }
};

