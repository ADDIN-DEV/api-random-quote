from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    "Hidup adalah petualangan yang berani.",
    "Kegagalan adalah kesuksesan yang tertunda.",
    "Berani gagal, berani sukses.",
    "Jangan pernah menyerah dalam meraih mimpi."
]

@app.route('/quote', methods=['GET'])
def get_quote():
    return jsonify({
        'quote': random.choice(quotes)
    })

if __name__ == '__main__':
    app.run(debug=True)
