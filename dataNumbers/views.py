from django.http import HttpResponse
from django.contrib.auth import authenticate


# Create your views here.
def index(request):
    user = authenticate(username='Pablito2020', password='adminroot')
    if user is not None:
        return HttpResponse("Authenticated! Yay!")
    else:
        return HttpResponse("Not authenticated! SadFace")
