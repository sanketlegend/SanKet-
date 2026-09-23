let display = document.getElementById("display");

let currentInput = "0";


function updateDisplay() {
    display.innerText = currentInput;
}


// Number / Operator

function appendValue(value) {

    if (currentInput === "0") {
        currentInput = value;
    } 
    else {
        currentInput += value;
    }

    updateDisplay();
}


// AC

function clearAll() {

    currentInput = "0";

    updateDisplay();
}


// C-CE

function clearEntry() {

    currentInput = "0";

    updateDisplay();
}


// Calculate

function calculate() {

    try {

        let expression = currentInput;

        // Percentage
        expression = expression.replace(
            /(\d+(?:\.\d+)?)%/g,
            "($1/100)"
        );

        let result = eval(expression);

        currentInput = String(result);

        updateDisplay();

    } 
    catch (error) {

        currentInput = "Error";

        updateDisplay();

        setTimeout(clearAll, 1000);
    }
}