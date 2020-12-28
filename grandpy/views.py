from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/livesearch', methods=['POST', 'GET'])
def livesearch():
    searchbox = request.form.get("text")
    return jsonify(searchbox)

if __name__ == "__main__":
    app.run(debug=True)