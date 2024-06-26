from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/roll', methods=['GET'])
def roll_dice():
    result = random.randint(1, 6)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
