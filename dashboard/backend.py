import os

import openai
from flask import Flask, jsonify, request

app = Flask(__name__)

openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/api/request', methods=['POST'])
def send_request():
    data = request.get_json()
    response = openai.ChatCompletion.create(
        model="gpt-3",
        messages=[
            {
                "role": "user",
                "content": data['content'],
            },
        ],
    )
    return jsonify(response)

@app.route('/api/response', methods=['GET'])
def get_response():
    response = openai.ChatCompletion.list()
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
