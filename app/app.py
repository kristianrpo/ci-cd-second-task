# app/app.py
"""
Main application file for the Flask web application.

This module initializes the Flask app, defines the main routes,
and serves as the entry point to run the development server.

"""
from flask import Flask, render_template, request
from .calculadora import sumar, restar, multiplicar, dividir
import os

app = Flask(__name__)


@app.get("/")
def index():
    """
    Display the calculator form (safe HTTP method).

    This route responds only to GET requests and is considered safe,
    as it does not alter the state of the application. It simply
    renders the calculator form without performing any calculation.

    Returns:
        str: Rendered HTML template (`index.html`) with no result.
    """
    return render_template("index.html", resultado=None)


@app.post("/calcular")
def calcular():
    """
    Process arithmetic calculations.

    This route handles POST requests and is considered unsafe since
    it processes user input and changes the application state by producing
    a calculated result. It retrieves two numbers and the chosen operation
    from the request form, executes the calculation, and renders the template
    with the computed result.

    Supported operations:
        - sumar
        - restar
        - multiplicar
        - dividir

    Exception Handling:
        - ValueError: Raised if input values are not valid numbers.
        - ZeroDivisionError: Raised if division by zero is attempted.

    Returns:
        str: Rendered HTML template (`index.html`).
    """
    resultado = None
    try:
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operacion = request.form["operacion"]

        if operacion == "sumar":
            resultado = sumar(num1, num2)
        elif operacion == "restar":
            resultado = restar(num1, num2)
        elif operacion == "multiplicar":
            resultado = multiplicar(num1, num2)
        elif operacion == "dividir":
            resultado = dividir(num1, num2)
        else:
            resultado = "Operación no válida"
    except ValueError:
        resultado = "Error: Introduce números válidos"
    except ZeroDivisionError:
        resultado = "Error: No se puede dividir por cero"

    return render_template("index.html", resultado=resultado)


@app.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    app_port = int(os.environ.get("PORT", 5000))
    app.run(port=app_port, host="0.0.0.0")  # pragma: no cover
