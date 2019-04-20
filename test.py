#!flask/bin/python
from flask import Flask, request, jsonify
import pymorphy2

morph = pymorphy2.MorphAnalyzer()
d = dict()
s = set()

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'})


# @app.route('/')
# def index():
#     return 'Index Page'


@app.route('/tags', methods=['POST'])
def test():
    sentences = request.data.decode("utf-8")
    sentences_list = sentences.split(' ')
    counter = 0

    for word in sentences_list:
        if len(word) > 1:
            p = morph.parse(word)[0]
            if p.tag.POS != 'NUMR' and p.tag.POS != 'NPRO' and p.tag.POS != 'PRED' and p.tag.POS != 'PREP' and p.tag.POS != 'CONJ' and p.tag.POS != 'PRCL' and p.tag.POS != 'INTJ':
                nf = p.normal_form
                if nf not in d.keys():
                    d[nf] = 1
                    s.update([p.normal_form])
                    counter += 1
                    print(counter)
                else:
                    d[nf] += 1

    # list_key_value = [[k, v] for k, v in d.items()]
    return jsonify({'tags': d})

# if __name__ == '__main__':
#     app.run(debug=True)
