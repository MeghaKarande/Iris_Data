
from flask import Flask, jsonify, render_template, request

from project_app.utils import IrisData

# Creating instance here
app = Flask(__name__)


@app.route("/") 
def hello_flask():
    print("Welcome to Flower Species Prediction System")   
    return render_template("index.html")


@app.route("/predict_charges", methods = ["POST", "GET"])
def get_sales_price():
    if request.method == "GET":
        print("We are in a GET Method")

        SepalLengthCm = float(request.args.get("SepalLengthCm"))
        SepalWidthCm  = float(request.args.get("SepalWidthCm"))
        PetalLengthCm = float(request.args.get("PetalLengthCm"))
        PetalWidthCm  = float(request.args.get("PetalWidthCm"))

        print("----- SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm -----")

        iris = IrisData(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)
        species = iris.get_predicted_species()

        return render_template("index.html", prediction = species)
    
print("__name__-->", __name__)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5001, debug = False)