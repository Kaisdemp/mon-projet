from flask import Flask, render_template, request, redirect
import database
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
database.init_db()

@app.route("/")
def accueil():
    return render_template("index.html")

@app.route("/creer", methods=["POST"])
def creer():
    question = request.form.get("question")
    # Les options arrivent comme option1, option2, option3...
    options = [v for k, v in request.form.items() if k.startswith("option") and v.strip()]
    code = database.creer_sondage(question, options)
    return redirect(f"/sondage/{code}")

@app.route("/sondage/<code>")
def voir_sondage(code):
    sondage = database.get_sondage_par_code(code)
    if sondage is None:
        return "Sondage introuvable", 404
    options = database.get_options(sondage["id"])
    return render_template("sondage.html", sondage=sondage, options=options)

@app.route("/voter/<code>", methods=["POST"])
def voter(code):
    option_id = request.form.get("option_id")
    database.ajouter_vote(option_id)
    return redirect(f"/resultats/{code}")

@app.route("/resultats/<code>")
def resultats(code):
    sondage = database.get_sondage_par_code(code)
    if sondage is None:
        return "Sondage introuvable", 404
    resultats = database.get_resultats(sondage["id"])
    return render_template("resultats.html", sondage=sondage, resultats=resultats)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
