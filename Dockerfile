FROM python:3.6.7-stretch

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /code:$PYTHONPATH
RUN echo 'alias ll="ls -lh"' >> ~/.bashrc
RUN echo 'alias ll="ls -la"' >> ~/.bashrc

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code
COPY requirements_dev.txt /code

RUN pip install -r requirements_dev.txt

COPY . /code/
