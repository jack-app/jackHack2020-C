from flask import Flask, request, jsonify
from flask_cors import CORS

from jackinator import Thothnator

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False
app.config['CORS_HEADERS'] = 'Content-Type'

thothnator = Thothnator()

@app.route('/', methods=['GET'])
def get_json_from_dictionary():
    dic = {
        'hello': 'world',
    }
    return jsonify(dic)

@app.route('/questions', methods=['GET'])
def get_quesion():
    q = thothnator.decideQ()
    thothnator.q_list.append(q)
    res = {"question": q}

    return jsonify(res)

@app.route('/answers', methods=['GET'])
def get_answer():
    # count = request.json('count')
    question = request.args.get('question')
    answer = int(request.args.get('answer'))
    thothnator.a_list.append(answer)
    thothnator.p = thothnator.updateP(thothnator.p, question, answer)

    if thothnator.isNeedContinueQ():
        result = ''
        res = {'continue': True, 'result': result}
    else:
        result = thothnator.getBestEstimate()
        thothnator.updateDatabase
        res = {'continue': False, 'result': result}

    return jsonify(res)

# @app.route('/questions', methods=['POST'])
# def post_question():
#     # count = request.json('count')
#     question = request.json['question']
#     answer = request.json['answer']
#     thothnator.a_list.append(answer)
#     thothnator.p = thothnator.updateP(thothnator.p, question, answer)

#     if thothnator.isNeedContinueQ():
#         result = ''
#         res = {'continue': True, 'result': result}
#     else:
#         result = thothnator.getBestEstimate()
#         thothnator.updateDatabase
#         res = {'continue': False, 'result': result}

#     return jsonify(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
