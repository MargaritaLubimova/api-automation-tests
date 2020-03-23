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
docker run -it -rm -p 4200:8000 --name my-running-app api-tests
```
##### During running docker container when all tests will pass open link in a browser to check the actual report [localhost:4200](http://localhost:4200)
#### Example of the report

#### Overview
<p align = "center">
    <img src = "./source/001.png">
</p>

#### Detailed report
<p align = "center">
    <img src = "./source/002.png">
</p>
