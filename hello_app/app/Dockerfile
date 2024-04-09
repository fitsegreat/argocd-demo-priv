FROM python:3.10.14-alpine

RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 5000
CMD [ "python", "/app/main.py" ]