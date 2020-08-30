from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

@app.route('/', methods=['GET'])
def get_json_from_dictionary():
    dic = {
        'hello': 'world',
    }
    return jsonify(dic)

@app.route('/questions', methods=['GET'])
def get_quesion():
    queries = request.args
    question = {"question": {"id": 1, "q": "aaa?", "ans": "yes", "end": False, "prediction": None}}
    return jsonify(question)

@app.route('/questions', methods=['POST'])
def post_question():
    json = request.get_json()
    return jsonify(json)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
