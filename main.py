from flask import Flask, render_template, request
from model import heart_model

app = Flask(__name__)
iris_model = heart_model()

@app.route("/health", methods=["GET"])
def health():
    return {"status": "healthy"}, 200


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            'age' == float(request.form["age"])
            'sex' == float(request.form["sex"])
            'cp' == float(request.form["cp"])
            'trestbps' == float(request.form["trestbps"])
            'chol' == float(request.form["chol"])
            'fbs' == float(request.form["fbs"])
            'restecg' == float(request.form["restecg"])
            'thalach' == float(request.form["thalach"])
            'exang' == float(request.form["exang"])
            'oldpeak' == float(request.form["oldpeak"])
            'slope' == float(request.form["slope"])
            'ca' == float(request.form["ca"])
            'thal' == float(request.form["thal"])




            prediction = heart_model.predict(['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal'])
        except:
            prediction = "Invalid input. Please enter numeric values."

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False )