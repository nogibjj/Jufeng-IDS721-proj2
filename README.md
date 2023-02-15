# IDS721 Project 2 Kubernetes based Continuous Delivery
- Create a customized Docker container from the current version of Python that deploys a simple python script.
- Push image to DockerHub, or Cloud based Container Registery (ECR)
- Project should deploy automatically to Kubernetes cluster
- Deployment should be to some form of Kubernetes service (can be hosted like Google Cloud Run or Amazon EKS, etc)


## week1
1. create a python script that can print all files in the current path
2. build it as a docker image
3. push image to docker hub

### steps
1. write the dockerfile
```
FROM python:latest

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "mylib/list_files.py", "/app"]
```
2. build docker image
```
docker build -t list-files .
```
3. run docker image
```
docker run list-files
```
4. push to docker hub
```
docker tag list-files <docker_hub_username>/<repository_name>:<tag>
docker login --username=<docker_hub_username>
docker push <docker_hub_username>/<repository_name>:<tag>
```
For me, the command is 
```
docker tag list-files hoodie361/list-files:latest
docker login --username=hoodie361
docker push hoodie361/list-files:latest
```
<img width="723" alt="image" src="https://user-images.githubusercontent.com/44468782/219129278-1940c85d-537b-462c-bee9-3a4c327e127c.png">


