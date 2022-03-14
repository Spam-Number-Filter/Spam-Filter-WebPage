from .settings import *
import django_heroku

DEBUG = False
ALLOWED_HOSTS = ["http://spamnumberfilter.herokuapp.com", "http://spamnumberfilter.herokuapp.com/"]

django_heroku.settings(locals())
