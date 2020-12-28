from flask import Flask, render_template, request, jsonify
from main import GrandPy
from gp_parser import GPParser

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/livesearch', methods=['POST', 'GET'])
def livesearch():
    searchbox = request.form.get("text")
    parser = GPParser()
    result = parser.parser(searchbox)
    # grandpy = GrandPy()
    # result = grandpy.main_coord(searchbox)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)