from flask import Flask, request, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Calsiee</title>
</head>
<body style="text-align:center; font-family:Arial;">
    <h1>Calsiee Calculator</h1>
    <form method="POST">
        <input name="expression" placeholder="Enter calculation" style="font-size:20px; width:200px;">
        <br><br>
        <button type="submit">Calculate</button>
    </form>
    <h2>{{result}}</h2>
</body>
</html>
"""

"""@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        try:
            expr = request.form["expression"]
            result = eval(expr)
        except:
            result = "Error"
    return render_template_string(html, result=result)

if __name__ == "__main__":
    app.run()"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Calsiee is live 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)