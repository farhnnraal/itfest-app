from flask import Flask, render_template

app = Flask(__name__)

# Using Jinja macros

# Project directory
# |- app.py
# |- templates/
# |    |- base.html
# |    |- index.html
# |    |- components/
# |        |- *components
# |- static/
# |    |- img/
# |        |- *images

# Start developing environment
# source venv/bin/activate
# python app.py

@app.route("/")
def index():
    sensors = [
        {"name": "...", "value": "..."}
    ]

    configuration = {"title": "Configuration", "icon": "/static/icon/svg/code.svg"}

    return render_template("index.html", config=configuration)

if __name__ == "__main__":
    app.run(debug=True)
    # app.run(debug=True, host="0.0.0.0")