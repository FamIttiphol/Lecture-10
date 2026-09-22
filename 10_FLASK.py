from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World! i Love This World'

if __name__ == '__main__':
    app.run(debug=True)