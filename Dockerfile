FROM python:3

COPY templates /usr/local/templates

COPY weather /usr/local/weather

COPY weatherdetector /usr/local/weatherdetector

COPY db.sqlite3 /usr/local 

ADD manage.py / templates / weather / weatherdetector / db.sqlite3 /

RUN pip install -r ../requirments.txt

RUN python manage.py runserver

EXPOSE 8080
