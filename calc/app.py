from flask import Flask, request
from .settings import VERSION

app = Flask(__name__)

@app.route("/")
def show(): 
    return "Connected to server", 200

@app.route("/gcd")
def gcd():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return {"result": gcd(a, b)}, 200

@app.route("/version")
def ver():
    return {"v": VERSION}, 200

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)