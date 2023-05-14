from flask import Flask, request

app = Flask(__name__)

@app.route('/<name>')
def index(name):
    return f'<h1>Hello {name}</h1>'

@app.route('/amaar')
def amar():
    return "amar"

if __name__ == '__main__':
    app.run(debug=True)