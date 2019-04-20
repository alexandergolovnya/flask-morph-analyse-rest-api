#!flask/bin/python
from flask import Flask, request, jsonify
import pymorphy2

morph = pymorphy2.MorphAnalyzer()
d = dict()
s = set()

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/test', methods=['POST'])
def test():
    sentenses = request.data

    for word in sentenses:
        p = morph.parse(word)[0]
        nf = p.normal_form
        if nf not in d.keys():
            d[nf] = 1
            s.update([p.normal_form])
        else:
            d[nf] += 1

    # return "Hello, World!"
    return jsonify({'tags': sentenses})


if __name__ == '__main__':
    app.run(debug=True)
