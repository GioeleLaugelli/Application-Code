from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>CIAO MONDO v.5.2</p>"
