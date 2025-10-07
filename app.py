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

materials = {
    "Configuration": {
        "name": "Configuration",
        "svg": "/static/icon/svg/code.svg",
        "alt": "configuration-icon",
    },
    "Patient Information": {
        "name": "Patient Information",
        "svg": "/static/icon/svg/patient.svg",
        "alt": "patient-icon",
    },
    "Nebulizer Settings": {
        "name": "Nebulizer Settings",
        "svg": "/static/icon/svg/nebulizer.svg",
        "alt": "nebulizer-icon"
    },
    "Medical Report": {
        "name": "Medical Report",
        "svg": "/static/icon/svg/report.svg",
        "alt": "medical-report-icon"
    },
    "About": {
        "name": "About",
        "svg": "/static/icon/svg/about.svg",
        "alt": "about-icon"
    }
}

support_materials = {
    "Show Password": {
        "svg": "/static/icon/svg/eye.svg",
        "alt": "show-password-icon"
    },
    "Hide Password": {
        "svg": "/static/icon/svg/eye-slash.svg",
        "alt": "hide-password-icon"
    },
    "Arrow": {
        "svg": "/static/icon/svg/arrow.svg",
        "alt": "arrow-icon"
    },
    "Download": {
        "svg": "/static/icon/svg/download.svg",
        "alt": "download-icon"
    }
}

@app.route("/configuration")
def configuration():
    return render_template(f"configuration/index.html", configuration_page = materials, configuration_support = support_materials)

@app.route("/dashboard")
def dashboard():
    return render_template(f"dashboard/index.html", dashboard_page = materials, dashboard_support = support_materials)

if __name__ == "__main__":
    app.run(debug=True)
    # app.run(debug=True, host="0.0.0.0")