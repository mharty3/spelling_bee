from flask import Flask, request, jsonify
import word_finder

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return """<h1>Spelling Bee Solver</h1>
              <p>This site is an API for helping you out 
               on the NYT Spelling Bee game.</p>"""


@app.route("/api/spelling_bee", methods=["GET"])
def find_words():
    
    # check if letters were provided. if so, assign it to variable
    # if not, display an error

    if 'letters' in request.args:
        letters = request.args['letters']
    else:
        return "Error: No letters provided. Please provide some letters."
    
    good_words = word_finder.word_finder(letters)
    pangrams = word_finder.find_pangrams(good_words)
    data = dict(pangrams=pangrams, all_words=good_words)

    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0')