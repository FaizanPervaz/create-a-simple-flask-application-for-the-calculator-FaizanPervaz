from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    print("I am inside home")
    return "Hello World ! I can make change in at router : /change"

@app.route("/change", methods=["GET"])
def change():
    print("I am inside change")
    return "Hello World ! I am changed"

@app.route("/change/add/<x>/<y>", methods=["GET"])
def add(x, y):
    print("I am inside add")
    try:
        num1 = int(x)
        num2 = int(y)
        result = num1 + num2
        return str(result)
    except ValueError:
        return "Invalid input. Please make sure both x and y are numbers."
    
@app.route("/change/sub/<x>/<y>", methods=["GET"])
def sub(x, y):
    print("I am inside sub")
    try:
        num1 = int(x)
        num2 = int(y)
        result = num1 - num2
        return str(result)
    except ValueError:
        return "Invalid input. Please make sure both x and y are numbers."

@app.route("/change/mul/<x>/<y>", methods=["GET"])
def mul(x, y):
    print("I am inside mul")
    try:
        num1 = int(x)
        num2 = int(y)
        result = num1 * num2
        return str(result)
    except ValueError:
        return "Invalid input. Please make sure both x and y are numbers."

@app.route("/change/div/<x>/<y>", methods=["GET"])
def mul(x, y):
    print("I am inside div")
    try:
        num1 = int(x)
        num2 = int(y)
        result = num1 / num2
        return str(result)
    except ValueError:
        return "Invalid input. Please make sure both x and y are numbers."

if __name__ == "__main__":
    # app.run (host= "0.0.0.0")
    app.run(debug=True)
