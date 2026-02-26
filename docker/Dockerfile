FROM python:3.10

WORKDIR /app

COPY app/ /app/

RUN pip install mysql-connector-python

CMD ["python", "app.py"]
