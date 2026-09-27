from flask import Flask, render_template

from content import PROFILE, DIMENSIONS, JOURNEY, EXPERIENCES, PROJECT_GROUPS, CONTACT

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
        profile=PROFILE,
        dimensions=DIMENSIONS,
        journey=JOURNEY,
        experiences=EXPERIENCES,
        project_groups=PROJECT_GROUPS,
        contact=CONTACT,
    )


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html", profile=PROFILE, contact=CONTACT), 404


if __name__ == "__main__":
    app.run(debug=True)
