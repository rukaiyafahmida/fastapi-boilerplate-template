FROM python:3.11

WORKDIR /codebase
 
COPY requirements.txt /codebase/requirements.txt

RUN pip install -r /codebase/requirements.txt

COPY . . 

EXPOSE 8081
