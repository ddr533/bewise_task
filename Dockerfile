FROM python:3.9
WORKDIR /app
RUN apt update && apt upgrade -y
COPY . .
RUN pip install -r requirements.txt --no-cache-dir
CMD python manage.py runserver 0.0.0.0:8000
