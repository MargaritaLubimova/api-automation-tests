# API_Automation_Tests
Tests for REST API: https://jsonplaceholder.typicode.com

# How to run

#### Go to the project folder and run

##### Build docker container
```bash
docker build -t api-tests .
```
##### Run docker container
```bash
docker run -it  -p 4200:8000 --name my-running-app api-tests
```
##### During running docker container after finish all tests open link in a browser 
```
http://127.0.0.1:4200
```
#### You can see an attached report example

#### Overview
<p align = "center">
    <img src = "./source/001.png">
</p>

#### Detailed report
<p align = "center">
    <img src = "./source/002.png">
</p>
