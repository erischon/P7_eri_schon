from flask import Flask, render_template, request, jsonify

from .main import GrandPy
from .gp_parser import GPParser
from .config import Config

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/livesearch', methods=['GET', 'POST'])
def livesearch():
    searchbox = request.form.get("text")
    grandpy = GrandPy()
    result = grandpy.main(searchbox)
    return jsonify(result)

@app.route('/testmap')
def testmap():
    config = Config()
    GKEY = config.GKEY
    return render_template('map_google.html', gkey=GKEY)

if __name__ == "__main__":
    app.run(debug=True)