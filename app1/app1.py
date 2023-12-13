
from flask import Flask, jsonify, request
import os
import base64

app = Flask(__name__)
def check_credentials(username, password):
   
    #k8s vars:
    expected_username = base64.b64encode(os.getenv("USERNAME").encode("ascii")).decode('ascii')
    expected_password = base64.b64encode(os.getenv("PASSWORD").encode("ascii")).decode('ascii')
    #docker vars:
    #expected_username = 'api-username'
    #expected_password = 'api-password'
    return username == expected_username and password == expected_password


@app.route('/api/data', methods=['GET'])
def get_data():
    
    try:

        auth_header = request.headers.get('Authorization')
        username, password = auth_header.split(':')
        if check_credentials(username, password):
            data = {'message': 'Hello from App1 with credentials!'}
        else:
            data = {'message': f'Wrong credentials get from app2: {username} {password}, expected from secret: {expected_username} {expected_password}, '}

    except Exception as e:
        data = {'message': 'app1 error' + str(e)}
    return jsonify(data)
    
    #data = {'message': 'app1 success'}
    #return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


"""

    try:
        
        expected_username = os.environ.get("USERNAME")
        expected_password = os.environ.get("PASSWORD")
        #expected_username = 'api-username'
        #expected_password = 'api-password'

        #auth_header = request.headers.get('Authorization')
        #username, password = auth_header.split(':')
        if str(expected_username) == str(username) and \
            str(expected_password) == str(password):
            data = {'message': 'Hello from App1!'}
        else:
            data = {'message': f'Wrong credentials get from app2: {username} {password}, expected from secret: {expected_username} {expected_password}, '}
    except Exception as e:
        data = {'message': 'app1 error' + str(e)}
"""