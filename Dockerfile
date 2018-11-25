FROM python:latest

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python python-pip

COPY /allSales /allSales/requirements.txt

RUN pip install -r /allSales/requirements.txt

CMD ["python", "/allSales/manage.py", "runserver", "0.0.0.0:8000"]