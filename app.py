from flask import Flask, render_template

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()

@app.route('/')
def home():
    return "Hello World!"
