from flask import Flask, render_template, redirect, request, jsonify
# from modelHelper import ModelHelper
# from sqlHelper import SQLHelper
import json


# Create an instance of Flask
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")

@app.route("/about")
def about():
    # Return template and data
    return render_template("about.html")

@app.route("/database")
def database():
    # Return template and data
    return render_template("database.html")

@app.route("/historical")
def historical():
    # Return template and data
    return render_template("historical.html")

@app.route("/predictions")
def predictions():
    # Return template and data
    return render_template("predictions.html")

@app.route("/tableau")
def tableau():
    # Return template and data
    return render_template("tableau.html")

@app.route("/project_details")
def project_details():
    # Return template and data
    return render_template("project_details.html")

#############################################################

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

#main
if __name__ == "__main__":
    app.run(debug=True)
