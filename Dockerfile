FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app

CMD python manage.py runserver 0.0.0.0:8000
