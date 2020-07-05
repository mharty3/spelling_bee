FROM python:3.7-alpine
RUN apk update && apk add build-base

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY /app .
EXPOSE 5000
CMD python app.py