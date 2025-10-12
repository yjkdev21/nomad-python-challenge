from flask import Flask, render_template, request
from extractors.wanted import extract_wanted_jobs

app = Flask(__name__)

db = {}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword in db:
        jobs = db[keyword]
    else:    
        jobs = extract_wanted_jobs(keyword)
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)


app.run("0.0.0.0")
