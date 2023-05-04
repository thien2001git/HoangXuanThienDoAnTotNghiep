from flask import Flask, url_for, render_template
# flask --app Main run --debug
app = Flask(__name__, static_folder='static',)

@app.route("/")
def index():
    return render_template("index.html")