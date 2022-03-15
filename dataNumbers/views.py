from django.http import HttpResponse
from django.contrib.auth import authenticate


# Create your views here.
from django.template import loader, Context
from django.views.generic import TemplateView


def index(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
