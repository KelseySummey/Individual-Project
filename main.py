from flask import Flask
from flask import jsonify

app = Flask(__name__)
@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World! My name is Kelsey Summey, and I like to make AI Apps!'

@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)

@app.route('/hi/<value>')
def hi(value):
        val = {"Hi, Welcome to Kelsey's App!": value}
        return jsonify(val)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
