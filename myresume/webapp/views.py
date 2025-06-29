from django.shortcuts import render
from django.views.generic import TemplateView
from about.models import About
from configurations.models import (Configurations, Stats,Skill, SkillData)
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
    #Make and object for the Stats and return it
    def get_stats_obj(self, *args, **kwargs):
        obj = Stats.objects.first()
        return obj
    
    #A bit different by making dictionaries and loop through methods
    def get_skill_obj(self, *args, **kwargs):
         """
        Returns *all* Skill rows, each with its related SkillData.
        [{ "skill": <Skill>, "data": <QuerySet> }, …]"""
         return(
            Skill.objects
            .prefetch_related("skilldata")        # 1 DB hit ‑› avoids N+1
            .all()
            .order_by("id")
            .values_list("id", flat=True)   
         )
       
       

    def get_context_data(self, *args, **kwargs):
        context =  super(HomePageTemplateView, self).get_context_data(** kwargs)
        context['about_objs'] = self.get_about_obj()
        context['configurations_obj'] = self.get_configurations_obj()
        context['stats_obj'] = self.get_stats_obj()
        
       
        # skill_blocks = [{ "skill": obj, "data": obj.skilldata.all() }, … ]
        skill_blocks = []
        for skill in Skill.objects.prefetch_related("skilldata").all():
            skill_blocks.append(
                {"skill": skill, "data": skill.skilldata.all()}
            )
        context["skill_blocks"] = skill_blocks
        # 
        #   #  {'skill': <Skill>, 'skillData': <QuerySet>
        return context
