import json
from flask import Flask


app = Flask(__name__)

@app.route('/')
def home():
    return json.dumps({})

@app.route('/test')
def test():
    return json.dumps({"message": "Success"})

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')