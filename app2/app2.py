
import requests
from flask import Flask
import os
import base64
from kubernetes import client, config

#render_template

app = Flask(__name__)

@app.route('/')
def display_data():
    try:

        #k8s vars:
        
        api_url = 'http://myapp-service:5000/api/data'  # 'myapp-service' odwołuje się do app1 korzystając z k8s
        username = base64.b64encode(os.getenv("USERNAME").encode("ascii")).decode('ascii')
        password = base64.b64encode(os.getenv("PASSWORD").encode("ascii")).decode('ascii')
        #username = 'api-username'
        #password = 'api-password'
        """
        #docker vars:
        api_url= 'http://app1:5000/api/data'  # 'app1' to nazwa kontenera z app1 w Docker Compose
        username = 'api-username'
        password = 'api-password'
        """

        headers = {'Authorization': username + ':' + password}
        response = requests.get(api_url, headers=headers)
        data = response.json()
        #return render_template('index.html', message=data['message'])
        #return f"from app1 API with credentials: {data['message']}"
        return f'username: {username}, type of username {type(username)==str}, password: {password}, type of password {type(password)==str}, message: {data["message"]}'
    except Exception as e:
        return "from app2 "+str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

