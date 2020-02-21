from django.shortcuts import HttpResponse,render_to_response
from django.template.loader import get_template
from .models import *
# Create your views here.



def choices_test(request):
    author = Author.objects.get(id=1)
    gender = author.gender1
    print(gender)
    gender = author.get_gender1_display()
    print(gender)
    return HttpResponse("choices_test")

