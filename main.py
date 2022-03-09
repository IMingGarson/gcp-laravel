from flask import Flask
from api.BaseMiddleware import BaseMiddleware

app = Flask(__name__)
app.wsgi_app = BaseMiddleware(app.wsgi_app)

@app.route('/')
def hello_world():
    return 'Flask Dockerized'

@app.route('/test')
def hello_test():
    return 'Flask Dockerized from test'

@app.route('/api/v1/all', methods=['GET'])
def show_v2():
    return 'API get all route v2'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=19999)