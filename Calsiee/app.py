from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
<title>Calsiee</title>
<style>
body {
    background: #1C1C1C;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}
.calculator {
    width: 250px;
}
.display {
    background: black;
    color: white;
    font-size: 30px;
    text-align: right;
    padding: 10px;
}
button {
    width: 60px;
    height: 60px;
    font-size: 20px;
    margin: 2px;
}
.row {
    display: flex;
}
</style>
</head>
<body>

<div class="calculator">
    <div id="display" class="display">0</div>

    <div class="row">
        <button onclick="clearAll()">AC</button>
        <button onclick="addValue('%')">%</button>
        <button onclick="addValue('/')">/</button>
    </div>

    <div class="row">
        <button onclick="addValue('7')">7</button>
        <button onclick="addValue('8')">8</button>
        <button onclick="addValue('9')">9</button>
        <button onclick="addValue('*')">x</button>
    </div>

    <div class="row">
        <button onclick="addValue('4')">4</button>
        <button onclick="addValue('5')">5</button>
        <button onclick="addValue('6')">6</button>
        <button onclick="addValue('-')">-</button>
    </div>

    <div class="row">
        <button onclick="addValue('1')">1</button>
        <button onclick="addValue('2')">2</button>
        <button onclick="addValue('3')">3</button>
        <button onclick="addValue('+')">+</button>
    </div>

    <div class="row">
        <button onclick="addValue('0')">0</button>
        <button onclick="addValue('.')">.</button>
        <button onclick="calculate()">=</button>
    </div>
</div>

<script>
let display = document.getElementById("display");

function addValue(val){
    if(display.innerText === "0") display.innerText = val;
    else display.innerText += val;
}

function clearAll(){
    display.innerText = "0";
}

function calculate(){
    try{
        display.innerText = eval(display.innerText);
    }catch{
        display.innerText = "Error";
    }
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)