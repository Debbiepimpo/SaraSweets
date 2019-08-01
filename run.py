import os
import json
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "some_secret"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About me!", company=data)

@app.route('/about/<saraSweets_name>')
def about_saraSweets(saraSweets_name):
    saraSweets = {}
    
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == saraSweets_name:
                saraSweets = obj
    
    return render_template("saraSweets.html", saraSweets=saraSweets)


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have receive your message!".format(
              request.form["name"]))
    return render_template("contact.html", page_title="Contact us!")


@app.route('/gallery')
def gallery():
    return render_template("gallery.html", page_title="Gallery", list_of_numbers=[1,2,3])


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)