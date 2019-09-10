from flask import Flask, render_template

"""
Python Flask Website
"""

flsk_obj = Flask(__name__)


@flsk_obj.route('/')
def home():
    return render_template("app_4_home.html")


@flsk_obj.route('/about/')
def about():
    return render_template("app_4_about.html")

if __name__ == "__main__":
    flsk_obj.run(debug=True)
