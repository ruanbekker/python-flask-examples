from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def main():
    payload = request.get_json(force=True)
    print(payload)
    return jsonify(payload)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
    
"""
Request:
========
$ curl -H "Content-Type: application/json" -XPOST http://localhost:5000/ -d '{"name": "ruan"}'

Response:
=========
{'name': 'ruan'}
"""
