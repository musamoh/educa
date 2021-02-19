# pull base image

FROM python:3.7



#Set enviromental variables

ENV PYTHONWRITE4BYTECODE 1
ENV PYTHONUNBUFFERED 1


#  Set work directory

WORKDIR /code


#install dependencies

COPY requirements.txt /code
# Install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/