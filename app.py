from flask import Flask, request, render_template, jsonify
import word_finder

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return """<h1>Spelling Bee Solver</h1>
              <p>This site is a prototype API for helping you out 
              (aka cheating) on the NYT Spelling Bee game.</p>"""


@app.route("/api/spelling_bee", methods=["GET"])
def api_id():
    # check if letters were provided. if so, assign it to variable
    # if not, display an error

    if 'letters' in request.args:
        letters = request.args['letters']
    else:
        return "Error: No letters provided. Please specify an id."
    
    good_words = word_finder.word_finder(letters)
    pangrams = word_finder.find_pangrams(good_words)
    data = dict(pangrams=pangrams, all_words=good_words)

    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0')