import math
from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<form method="post">
  <input type="number" name="a" placeholder="Первое число">
  <input type="number" name="b" placeholder="Второе число">
  <select name="op">
    <option value="add">+</option>
    <option value="sub">-</option>
    <option value="mul">*</option>
    <option value="div">/</option>
    <option value="exp">^</option>
    <option value="per">%</option>
    <option value="sqrt">√</option>
    <option value="sin">Sin</option>
    <option value="cos">Cos</option>
    <option value="log">Log</option>
  </select>
  <button type="submit">Посчитать</button>
</form>
<p>Результат: {{ result }}</p>
"""


@app.route("/", methods=["GET", "POST"])
def calc():
    result = ""
    if request.method == "POST":
        a = float(request.form["a"])
        b = float(request.form["b"])
        op = request.form["op"]
        if op == "add":
            result = a + b
        elif op == "sub":
            result = a - b
        elif op == "mul":
            result = a * b
        elif op == "div":
            result = a / b if b != 0 else "Ошибка: деление на 0"
        elif op == "exp":
            result = a**b
        elif op == "per":
            result = a * b / 100
        elif op == "sqrt":
            result = math.sqrt(a) if a >= 0 else "Ошибка: отрицательное число"
        elif op == "sin":
            result = math.sin(math.radians(a))
        elif op == "cos":
            result = math.cos(math.radians(a))
        elif op == "log":
            result = math.log(a) if a > 0 else "Ошибка: число должно быть больше 0"

    return render_template_string(HTML, result=result)


if __name__ == "__main__":
    app.run(debug=True)
