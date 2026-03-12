from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    results = None

    if request.method == "POST":

        location = request.form.get("location")

        results = {
            "location": location,
            "temperature": 29,
            "air_quality": "Moderate",
            "sargassum": "Low risk",
            "seismic": "No recent activity"
        }

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)