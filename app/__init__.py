from flask import Flask , render_template 

app = Flask(__name__)

@app.route("/")
def index() :
    return "<centre><h1>Projet Rihaaab </h1></centre"


if __name__ == "__name__":
    app.run()