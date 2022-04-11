FROM python:alpine
COPY . /app
WORKDIR /app
ENV PYTHONUNBUFFERED=1
RUN pip install pip==21.3.1
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
RUN python manage.py makemigrations
