from django.urls import path
from .views import *
urlpatterns = [
    path('choices_test/', choices_test),

]
