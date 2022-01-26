FROM python:3.9.9
RUN mkdir /goodVibes
WORKDIR "/goodVibes"
COPY ./requirements.txt .
RUN pip install -r requirements.txt