from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return 'Hello, World!'

@app.route('/test', methods=['POST'])
def test():
    print(request.get_json())
    # with open("open-minds-repo\open-minds-solution\summarize.py") as f:
        # exec (f.read())
    return '', 204


