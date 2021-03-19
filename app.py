from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def predict():
    RF_model = open('rf_grid.pkl','rb')
    model = joblib.load(RF_model)
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])
    output = int(prediction[0])
    result = {'Survived':output}
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
