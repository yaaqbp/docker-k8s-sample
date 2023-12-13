# docker-k8s-sample
Current work:

0. pull repo

to check work in docker:
1. change "api_url" variable in app2.py to use 'app1' in http
2. "docker compose build"
3. "docker compose up"
4. go to localhost:5001 - there is visible data that app2 get from app1 

to use in k8s:
it was created using minikube:
1. minikube start
2. minikube tunnel (in other terminal, has to work all the time)
3. kubectl apply -f ./kubernetes
4. go to localhost:5001 - there is visible data that app2 get from app1 
