from flask import Flask

app = Flask(__name__)


@app.get("/")
def index():
    return {"mensagem": "API de chamados em funcionamento"}, 200
