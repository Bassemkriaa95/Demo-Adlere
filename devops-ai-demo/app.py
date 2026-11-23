from flask import Flask

app = Flask(__name__)


@app.get("/")
def home():
    # TODO pour le demo : corriger l'erreur NameError sur jsonify.
    return jsonify({"message": "Demo DevOps AI", "status": "ok"})


if __name__ == "__main__":
    # TODO pour le demo : en conteneur, 127.0.0.1 n'est pas accessible depuis l'hôte.
    app.run(host="127.0.0.1", port=5000)
