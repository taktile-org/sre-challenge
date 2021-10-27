# Taktile SRE Challenge

Your challenge is to deploy a python workload on Kubernetes.

## Instructions
The goal is to deploy the application from the `app` directory to a 
local Kubernetes cluster. 

Two versions of the python application should be available, with 
different resource constraints. Both should be available from within
the `default` namespace under specific domain names:

1. A version that outputs the square series (`SERIES_VERSION=square`)
   - Resource limits: 100m CPU, 100Mi RAM
   - Available as `http://square`
2. A version that outputs the fibonacci series (`SERIES_VERSION=fibonacci`)
   - Resource limits: 200m CPU, 200Mi RAM
   - Available as `http://fibonacci`


To get started with the application (in this case the `square` version):
```
pip install -r app/requirements.txt
SERIES_VERSION=square uvicorn --host 0.0.0.0 --app-dir app main:app
```
To test the application:
```
curl localhost:8000/series?n=5
```
```
{"square": 25}
```

You may improve upon or modify the elements that are already present, as you see fit.

## Objectives
We give roughly equal weight to each of the following:

- Functionality 
- Simplicity
- Readability
- Extensibility 
- Maintainability
- Observability

Please don't stress if your solution isn't perfect, or is incomplete. 
With the given time constraints, you won't be able to tick all the boxes
above. This challenge is intended as an exercise in tradeoffs. 
We want to understand how you approach platform building.

