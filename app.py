from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Ema cosa dobbiamo fare per settimana prossima??</p>"
 
 
 
