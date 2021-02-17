# python-rest-api-docker

steps to run the sample rest service on docker -

1. Clone the Repository - git clone https://github.com/chorajesh/mlapi.git

2. Move to the directory - cd mlapi

3. Build the docker image - docker build -t mlapi-rest .

4. Create and run a container - docker run -d -p 5001:5000 mlapi-rest

5. Navigate to http://0.0.0.0:5001/predict

The actual api in the docker container is running on the port 5000 but we exposed the 5000 as 5001 on the host that contains the docker. 
