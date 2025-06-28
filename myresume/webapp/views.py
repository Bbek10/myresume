from django.shortcuts import render
from django.views.generic import TemplateView
from about.models import About
from configurations.models import Configurations
# Create your views here.
class HomePageTemplateView(TemplateView):  # Inheriting from TemplateView
    template_name = "index.html"

    def get_about_obj(self, *args, **kwargs):
        obj = About.objects.first()
        return obj
    
    #Make an object for the Configurations and return it 
    def get_configurations_obj(self, *args, **kwargs):
        obj = Configurations.objects.first()
        return obj  
         
    def get_context_data(self, *args, **kwargs):
        context =  super(HomePageTemplateView, self).get_context_data(** kwargs)
        context['about_objs'] = self.get_about_obj()
        context['configurations_obj'] = self.get_configurations_obj()
        return context  
