Pre-requisites
==============

0. AWS account.
1. Install [Docker 1.12](https://www.docker.com/products/overview)
  * OSX: Docker for Mac
  * Windows: Docker for Windows
  * Linux: Docker for Linux
2. Install [AWS CLI](https://aws.amazon.com/cli/)

Challenge
=========

1. Create an HTTP server with the route `GET:magicnight` that should
   return a JSON response as: `{ "response": "hello magic night!" }`
   (Hint: use pre-made [Python's server](../magicnight-app/server.py))

2. Create a Docker image with your HTTP server. (Hint: If you used the
   Python server, to create a custom Docker Image that has Python 2.7
   on it and your REST server and its dependencies there is an
   official Python 2.7 image on Docker Hub that you can use as
   baseline).

3. Publish your new image to [AWS Container Registry](https://aws.amazon.com/ecr/)

4. Run your Docker container on
   [AWS Elastic Container Service (ECS)](https://aws.amazon.com/ecs/)
   (Hint: Consult the
   [AWS ECS Developer Guide](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-dg.pdf) for: Amazon ECS Optimized AMI, AWS IAM roles needed, EC2 instances, ECS cluster, ECS Task definitions, ECS Services)
   
5. Confirm you can hit your end-point from the outside world.

Extra point #1
==============
Load balance your HTTP server.

Extra point #2
==============
Make both your ECS task and your EC2 instane containers' host auto
scalable.

Glossary
========

Docker
------
Package format that allows for easier deployment of applications.

Docker Image
------------
Specification of what is a container made of.

Docker Container
----------------
A running instance of a Docker Image.

ECS Container instance
----------------------
An Amazon EC2 instance that is running the Amazon ECS agent and has
been registered into an ECS cluster.

ECS Cluster
-----------
A logical grouping of container instances that you can place tasks on.

ECS Task definition
-------------------
A description of an application that contains one or more container
definitions.

ECS Task
--------
An instantiation of a task definition that is running on a container instance.

ECS Service
-----------
An Amazon ECS service allows you to run and maintain a specified number of instances of a task
definition simultaneously.




