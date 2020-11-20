import sys, os
from flask import Flask

app = Flask(__name__)

#route pour la page d'accueil
@app.route("/")
def index():
    return "Hello World!"

#run le http
if __name__ == "__main__":
    app.run(port=80)
