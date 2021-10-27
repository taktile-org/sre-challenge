# Taktile SRE Challenge

Your challenge is to automate and instrument the deployment of a python workload on Kubernetes.

## Description

The `app` directory contains a simple application, written in python. We would
like you to automate the deployment of this application. In particular, we are
interested in automatically assuring that the application reaches a running
state, and learning about how it performs. 

To get started with the application:
```
pip install -r app/requirements.txt
uvicorn  --app-dir app main:app --reload
curl localhost:8000/fibonacci?n=5
```



## Instructions

Fork this repository.

Feel free to use any tools at your disposal, but please provide a manifest of those 
tools (or an install script). 

You may improve upon or modify the elements that are already present, as you see fit.

Commit your configuration and code, and send us a link to your fork within one week.


## Timebox
Please don't spend more than 2 hours on your solution.
We give roughly equal weight to each of the following:

* Correctness
* Simplicity
* Readability
* Extensibility
* Maintainability
* Observability
* Ease of use
* Documentation


Please don't stress if your solution isn't perfect, or is incomplete. With
a timebox of at most 2 hours, you won't be able to tick all the boxes above.
This challenge is intended as an exercise in tradeoffs. We want to understand
how you approach platform building.


