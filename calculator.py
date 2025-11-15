@app.route("/", methods=["GET", "POST"])
def calc():
    result = ""
    if request.method == "POST":
        a_str = request.form["a"]
        b_str = request.form["b"]

        # преобразуем только если введено
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
