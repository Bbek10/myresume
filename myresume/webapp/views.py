from django.shortcuts import render
from django.views.generic import (
    TemplateView
)
# Create your views here.
class HomePageTemplateView(TemplateView): #TemplateView lai inherit garya class le
    template_name = "index.html"

