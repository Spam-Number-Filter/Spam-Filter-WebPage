FROM python:slim
RUN pip install pip==21.3.1
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
RUN python manage.py makemigrations
RUN python manage.py migrate --run-syncdb 
RUN python manage.py migrate
