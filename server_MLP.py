from flask import Flask, request, jsonify
from flask.templating import render_template

import back_MLP

app = Flask(__name__)

@app.route("/")
def index():
   	return render_template("app.html")

@app.route('/classify_image', methods = ['GET'])
def classify_image():
    image_data = request.form['image_data']

    response = jsonify(back_MLP.classify_image(image_data))

    response.headers.add('Access-Control-Allow-Origin','*')

    return  response
    

if __name__ == "__main__":
    back_MLP.load_saved_model()
    app.run(port=3000, debug=True)
