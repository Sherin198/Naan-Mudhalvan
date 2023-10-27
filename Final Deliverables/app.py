from flask import Flask,render_template

app=Flask(_name_)

@app.route("/")
def home():
    return render_template("index.html")

if _name=="main_":
    app.run(debug=True)
