from flask import Flask, request
import operations

app = Flask(__name__)

math = {
    "add": operations.add,
    "sub": operations.sub,
    "mult": operations.mult,
    "div": operations.div
}

operation_symbols = {
    "add": "+",
    "sub": "-",
    "mult": "x",
    "div": "%"
}


@app.route("/add")
def add():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{a} + {b} = {operations.add(a, b)}"


@app.route("/sub")
def sub():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{a} - {b} = {operations.sub(a, b)}"


@app.route("/mult")
def mult():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{a} * {b} = {operations.mult(a, b)}"


@app.route("/div")
def div():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{a} / {b} = {operations.div(a, b)}"


@app.route("/math/<operation>")
def calculator(operation):
    a = int(request.args["a"])
    b = int(request.args["b"])

    return f"<h1>{a} {operation_symbols[operation]} {b} = {math[operation](a, b)}</h1>"
