"""
# app2/app2.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from App 2!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)


"""

import requests
from flask import Flask
#render_template

app = Flask(__name__)

@app.route('/')
def display_data():
    try:
        #api_url= 'http://app1:5000/api/data'  # 'app1' to nazwa kontenera z app1 w Docker Compose
        api_url = 'http://myapp-service:5000/api/data'  # 'myapp-service' odwołuje się do app1 korzystając z k8s
        response = requests.get(api_url)
        data = response.json()
        #return render_template('index.html', message=data['message'])
        return f"from app1 API: {data['message']}"
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)


