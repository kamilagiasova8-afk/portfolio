from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

profile = {
    "name": "카밀라",
    "job": "명지대 학생",
    "age": "20살"
}

@app.route("/")
def home():
    return render_template("home.html", profile=profile)

app = app
