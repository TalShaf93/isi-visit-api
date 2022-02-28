# Base Image is set to Alpine - linux
#FROM python:3.6.1-alpine  -  dependencies problemes,  installing python 3.8 insted 
FROM python:3.8
# craete work directory
WORKDIR /ISI-assignment-api
# copy all the folder content indo the docker work directory 
ADD . /ISI-assignment-api
# install all the app dependencies 
RUN pip install -r requirements.txt
# container start command
CMD ["python", "api.py"]