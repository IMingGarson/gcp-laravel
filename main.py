from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Flask Dockerized'

@app.route('/test')
def hello_world():
    return 'Flask Dockerized from test'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)