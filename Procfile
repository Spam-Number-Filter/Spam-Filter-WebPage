release: sh -c 'python manage.py migrate --run-syncdb && python manage.py migrate'
web: gunicorn number_filter.wsgi
