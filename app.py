from flask import Flask, render_template
from datetime import datetime
from phrasal_verb import definition, generated_verb
from burgeramt import (
    dialogue_part1,
    dialogue_part2,
    dialogue_part3,
    dialogue_part4,
    dialogue_part5,
    dialogue_part6,
    dialogue_part7,
)
from hrrejection import hr_part1, hr_part2, hr_part3, hr_part4, hr_part5, hr_part6
from seinfeld import seinf_part1, seinf_part2, seinf_part3, seinf_part4

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", current_year=datetime.now().year)

@app.route("/previous")
def previous():
    return render_template("previous.html", current_year=datetime.now().year)

@app.route("/webapps")
def webapps():
    return render_template("webapps.html", current_year=datetime.now().year)

@app.route("/contact")
def contact():
    return render_template("contact.html", current_year=datetime.now().year)

@app.route("/wacky")
def wacky():
    return render_template("wacky.html", current_year=datetime.now().year)

@app.route("/phrasal_verb")
def phrasal_verb():
    return render_template(
        "phrasal_verb.html", data={"definition": definition(), "verb": generated_verb()}
    )

@app.route("/burgeramt")
def burgeramt():
    return render_template(
        "burgeramt.html",
        data={
            "part1": dialogue_part1(),
            "part2": dialogue_part2(),
            "part3": dialogue_part3(),
            "part4": dialogue_part4(),
            "part5": dialogue_part5(),
            "part6": dialogue_part6(),
            "part7": dialogue_part7(),
        },
    )

@app.route("/hrrejection")
def hrrejection():
    return render_template(
        "hrrejection_input.html",
        data={
            "hr_part1": hr_part1(),
            "hr_part2": hr_part2(),
            "hr_part3": hr_part3(),
            "hr_part4": hr_part4(),
            "hr_part5": hr_part5(),
            "hr_part6": hr_part6(),
        },
    )

@app.route("/seinfeld")
def seinfeld_opening():
    return render_template(
        "seinfeld_opening.html",
        data={
            "seinf_part1": seinf_part1(),
            "seinf_part2": seinf_part2(),
            "seinf_part3": seinf_part3(),
            "seinf_part4": seinf_part4(),
        },
    )

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 80))
    app.run(host="0.0.0.0", port=port)
