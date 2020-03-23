FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

# Install Python

RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip install --no-cache-dir -r requirements.txt

# Install Allure

RUN apt-get install sudo
RUN sudo apt-get install -y software-properties-common
RUN sudo apt-add-repository ppa:qameta/allure
RUN sed -i 's/focal/xenial/g' /etc/apt/sources.list.d/qameta-ubuntu-allure-focal.list
RUN sudo apt-get update --allow-insecure-repositories
RUN sudo apt-get install -y --allow-unauthenticated allure
RUN sudo apt-get install -y nodejs npm && npm install -g allure-commandline --save-dev

COPY . .

CMD bash in_docker_run.sh
