
"""
    
# app1/app1.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from App 1!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



"""

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'Hello from App1!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
