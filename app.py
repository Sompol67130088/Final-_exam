from flask import Flask, render_template, request, redirect
from db import get_all_references, add_reference, delete_reference

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", name="SompolC", student_id="640510XXX", github="https://github.com/SompolC/FinalExam")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/myresearch")
def myresearch():
    references = get_all_references()
    return render_template("myresearch.html", references=references)

@app.route("/reference", methods=["GET", "POST"])
def reference():
    if request.method == "POST":
        title = request.form["title"]
        pdf_url = request.form["pdf_url"]
        add_reference(title, pdf_url)
        return redirect("/reference")
    references = get_all_references()
    return render_template("reference.html", references=references)

@app.route("/delete/<int:id>")
def delete(id):
    delete_reference(id)
    return redirect("/reference")

if __name__ == "__main__":
    app.run(debug=True)