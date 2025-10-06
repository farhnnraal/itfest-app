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

# @app.route("/")
# def index():
#     return render_template("index.html")

@app.route("/configuration/<step>")
def configuration_steps(step):
    configuration = {"title": "Configuration", "icon": "/static/icon/svg/code.svg"}

    return render_template(f"configuration/{step}.html", config=configuration)

@app.route("/dashboard")
def dashboard():
    materials = [
        {
            "title": "Patient Information",
            "icon": "/static/icon/svg/patient.svg",
            "intractIcon": "/static/icon/svg/arrow.svg",
            "intractIconAlt": "Arrow-expand-inpand"
        },
        {
            "title": "Nebulizer Settings",
            "icon": "/static/icon/svg/nebulizer.svg",
            "intractIcon": "/static/icon/svg/arrow.svg",
            "intractIconAlt": "Arrow-expand-inpand"
        },
        {
            "title": "Medical Report",
            "icon": "/static/icon/svg/report.svg",
            "intractIcon": "/static/icon/svg/download.svg",
            "intractIconAlt": "Arrow-expand-inpand"
        },
        {
            "title": "About",
            "icon": "/static/icon/svg/about.svg",
            "intractIcon": "/static/icon/svg/arrow.svg",
            "intractIconAlt": "Arrow-expand-inpand"
        }
    ]

    return render_template(f"dashboard/index.html", config=materials)

if __name__ == "__main__":
    app.run(debug=True)
    # app.run(debug=True, host="0.0.0.0")