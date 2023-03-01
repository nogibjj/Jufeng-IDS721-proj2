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

## week2
1. Created the ECR repository and push the image to the repo.
2. Successfully create the EKS cluster and the node group.
3. Successfully depoly the app in EKS cluster.

<img width="1341" alt="image" src="https://user-images.githubusercontent.com/44468782/220737414-a9014961-6ea6-494d-bf97-6f2430278b87.png">
<img width="1346" alt="image" src="https://user-images.githubusercontent.com/44468782/220737555-862912a4-e720-4497-be1f-cc2df368762b.png">
<img width="835" alt="image" src="https://user-images.githubusercontent.com/44468782/220737649-64b06c8c-530f-4efb-a03c-77b150b6e042.png">
<img width="565" alt="image" src="https://user-images.githubusercontent.com/44468782/220737693-a41e4455-e0a1-49cc-ba52-5824609ff985.png">
we can see the service
<img width="960" alt="image" src="https://user-images.githubusercontent.com/44468782/220737800-d602ef8b-b43f-4f82-940b-6fc837ede62a.png">

2. Successfully create the EKS cluster and the node group.


## week3
switch to minikube method

1. ```minikube start```

<img width="696" alt="image-20230301135102358" src="https://user-images.githubusercontent.com/44468782/222240857-325ec6b2-f091-426b-87d8-81fc03dd4496.png">


2. push docker image to DockerHub

   ```
   docker tag fast-api hoodie361/fast-api:latest
   docker push hoodie361/fast-api:latest
   ```

3. Create a deployment

   ```
   kubectl create deployment fast-api --image=registry.hub.docker.com/hoodie361/fast-api
   ```

4. Run `kubectl get deployments` to view deployments

<img width="430" alt="image-20230301135449636" src="https://user-images.githubusercontent.com/44468782/222240910-b61d675a-ab59-4c19-824f-46a93728db7b.png">


5. Run `kubectl get pods` to see the status of pods

<img width="560" alt="image-20230301135504592" src="https://user-images.githubusercontent.com/44468782/222240938-bd789b64-8a91-4e62-a8f3-cc4660c67ab8.png">


6. Create service and expose it: `kubectl expose deployment hello-node --type=LoadBalancer --port=8080`

<img width="584" alt="image-20230301135539893" src="https://user-images.githubusercontent.com/44468782/222240963-4c7f678f-23f3-40e9-a69d-2f1ab44ca85d.png">


7. View services:  `kubectl get services`

<img width="583" alt="image-20230301135558701" src="https://user-images.githubusercontent.com/44468782/222240994-1db2542a-33b7-4e61-b434-1ac830d52cf1.png">


8. check the service run where: `minikube service fast-api --url`

<img width="345" alt="image-20230301135932651" src="https://user-images.githubusercontent.com/44468782/222241016-2804a26c-c9a4-4b1f-9a8c-475dcdb69ad3.png">

9. visit the service , e.g., send a http request curl `http://127.0.0.1:56806/fruit`

<img width="348" alt="image-20230301140022071" src="https://user-images.githubusercontent.com/44468782/222241053-11b1453c-bd7e-4861-bbe4-e35a19dece7e.png">


