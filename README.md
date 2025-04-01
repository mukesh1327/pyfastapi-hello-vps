# Python FastAPI hello world - Noventiq value point

__A demo hello world python fastAPI application__

___Running on port :___ 9002

___Endpoints :___   
    /vps-welcome   
    /vps-welcome/hello

___Environment variables :___   
APP_TITLE=string


## How to run in local

uvicorn main:app --host 0.0.0.0 --port 9002 --reload

## Run as container

podman build -t pyfastapi-hello:v1.0 -f .\Dockerfile .

podman run -d -p 9002:9002 --name pyfast-hello pyfastapi-hello:v1.0

## Deploy in k8s-ocp

oc apply -f ./k8s-manifests -n demo-namespace