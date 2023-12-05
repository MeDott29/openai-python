import os
import openai
from flask import Flask, jsonify, request

app = Flask(__name__)

# Initialize the OpenAI client
client = openai.OpenAI()

@app.route('/api/request', methods=['POST'])
def send_request():
    content = request.form['content']
    response = openai.ChatCompletion.create(
        model="gpt-3",
        messages=[
            {
                "role": "user",
                "content": content,
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

@app.route('/api/request', methods=['POST'])
def send_request():
    content = request.form['content']
    response = openai.ChatCompletion.create(
        model="gpt-3",
        messages=[
            {
                "role": "user",
                "content": content,
            },
        ],
    )
    return jsonify(response)

@app.route('/api/response', methods=['GET'])
def get_response():
    response = openai.ChatCompletion.list()
    return jsonify(response)

