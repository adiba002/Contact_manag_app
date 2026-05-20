from flask import Flask, render_template, request, redirect

app = Flask(__name__)

contacts = []

@app.route("/")
def home():
    return render_template("index.html", contacts=contacts)

@app.route("/add", methods=["POST"])
def add():
    first = request.form["first"]
    last = request.form["last"]
    email = request.form["email"]
    phone = request.form["phone"]

    if "@" not in email:
        return "Invalid Email"

    contacts.append({
        "first": first,
        "last": last,
        "email": email,
        "phone": phone
    })

    return redirect("/")

@app.route("/delete/<int:index>")
def delete(index):
    contacts.pop(index)
    return redirect("/")

@app.route("/edit/<int:index>")
def edit(index):
    contact = contacts[index]
    return render_template("edit.html", contact=contact, index=index)

@app.route("/update/<int:index>", methods=["POST"])
def update(index):
    contacts[index] = {
        "first": request.form["first"],
        "last": request.form["last"],
        "email": request.form["email"],
        "phone": request.form["phone"]
    }
    return redirect("/")

app.run(debug=True)
