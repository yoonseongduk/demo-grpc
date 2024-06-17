# lucida-kcmagent



## Getting started

## master.proto - compile (\w python)

```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. master.proto
```


## Docker image build

```
# master pod - image build
docker build -t your-docker-repo/master:latest -f master.Dockerfile .

# agent pod - image build
docker build -t your-docker-repo/agent:latest -f agent.Dockerfile .
```


## Docker image push

```
docker push your-docker-repo/master:latest
docker push your-docker-repo/agent:latest
```

## Kubernetes - deploy 

```
kubectl apply -f master-service.yaml
kubectl apply -f master-pod.yaml
kubectl apply -f agent-pod.yaml
```
