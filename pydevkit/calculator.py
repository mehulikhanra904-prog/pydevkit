def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")

    return a / b


def calculate(expression: str) -> float:
    expression = expression.replace(" ", "")

    for operator in ["+", "-", "*", "/"]:
        if operator in expression:
            parts = expression.split(operator)

            if len(parts) != 2:
                raise ValueError("Invalid expression.")

            first_number = float(parts[0])
            second_number = float(parts[1])

            if operator == "+":
                return add(first_number, second_number)

            if operator == "-":
                return subtract(first_number, second_number)

            if operator == "*":
                return multiply(first_number, second_number)

            if operator == "/":
                return divide(first_number, second_number)

    raise ValueError("Use an expression such as 20+80.")