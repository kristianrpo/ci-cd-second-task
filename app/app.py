# app/app.py
"""
Main application file for the Flask web application.

This module initializes the Flask app, defines the main routes,
and serves as the entry point to run the development server.

"""
from flask import Flask, render_template, request
from .calculadora import sumar, restar, multiplicar, dividir

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Handle the root route of the calculator application.

    Supports both GET (to display the form) and POST (to process calculations).
    Retrieves two numbers and an operation from the form, performs the
    requested arithmetic calculation, and renders the result.

    Returns:
        str: Rendered HTML template (index.html).
    """
    resultado = None
    if request.method == "POST":
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


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
