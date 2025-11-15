import math
from flask import Flask, request, render_template_string

# сначала создаём приложение
app = Flask(__name__)

# потом пишем HTML
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


# только после этого пишем маршруты
@app.route("/", methods=["GET", "POST"])
def calc():
    result = ""
    if request.method == "POST":
        a_str = request.form["a"]
        b_str = request.form["b"]

        a = float(a_str) if a_str else 0
        b = float(b_str) if b_str else None

        op = request.form["op"]

        if op == "add":
            result = a + (b if b is not None else 0)
        elif op == "sub":
            result = a - (b if b is not None else 0)
        elif op == "mul":
            result = a * (b if b is not None else 0)
        elif op == "div":
            result = a / b if b not in (None, 0) else "Ошибка: деление на 0"
        elif op == "exp":
            result = a**b if b is not None else "Ошибка: нужно два числа"
        elif op == "per":
            result = a * b / 100 if b is not None else "Ошибка: нужно два числа"
        elif op == "sqrt":
            result = math.sqrt(a) if a >= 0 else "Ошибка: отрицательное число"
        elif op == "sin":
            result = math.sin(math.radians(a))
        elif op == "cos":
            result = math.cos(math.radians(a))
        elif op == "log":
            if b is None:
                result = math.log(a) if a > 0 else "Ошибка: число должно быть > 0"
            else:
                result = (
                    math.log(a, b)
                    if a > 0 and b > 0 and b != 1
                    else "Ошибка: неверное основание"
                )

    return render_template_string(HTML, result=result)


# запуск приложения
if __name__ == "__main__":
    app.run(debug=True)
