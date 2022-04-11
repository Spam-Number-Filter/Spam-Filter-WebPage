""" File that conatinas the controller of MVC,
the code controlling the business logic of the application. """

from django.http import HttpResponse

# Create your views here.
from django.template import loader


def index(request):
    """Controller of the index page."""
    template = loader.get_template("home.html")
    return HttpResponse(template.render())
