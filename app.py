import pymorphy2
import json
from flask import Flask, request

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return


@app.route('/')
def book_create():
    data = request.json

    # params = {
    #     'title': data['title'],
    #     'author_id': data['author_id']
    # }

    return data

if __name__ == '__main__':
    app.run(debug=True)
