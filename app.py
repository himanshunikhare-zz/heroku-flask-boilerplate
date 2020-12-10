import flask
import pandas as pd
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    d = {'col1': [1,123, 2], 'col2': [3,23, 4]}
    df = pd.DataFrame(data=d)
    return jsonify(df.to_dict())

app.run()
