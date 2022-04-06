from django.contrib.auth import authenticate
from django.http import HttpResponse

# Create your views here.
from django.template import Context, loader
from django.views.generic import TemplateView


def index(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())
