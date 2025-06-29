from django.db import models

# Create your models here.
class Configurations(models.Model):
    #according to the fields that are in the front end 

    #name - Bibek Manandhar
    name = models.CharField(
        'name',
        max_length=25
    )

    # typed animation 
    typed = models.CharField(
        'typed',
        max_length=255,
        help_text="Type like -> an Engineer, Project Manager, Yoga Instructor"
    )

    #   git link
    git = models.URLField(
        'github link'
    )

    # facebook link
    facebook = models.URLField(
        'facebook link'
    )

    # insta link 
    insta = models.URLField(
        'insta link'
    )

    # strava
    strava = models.URLField(
        'strava link'
    )

    # linkedIn 
    linkedIn = models.URLField(
        'linkedIn link'
    )

    def __str__(self,*args, **kwargs):
        return f"{self.id}{self.name}"
    
    def __unicode__(self, *args, **kwargs):
        return f"{self.id}{self.name}"

class Stats(models.Model):

    # Stats name change
    name = models.CharField(
        'name'
    )

    paragraph = models.TextField(
        'paragraph'
    )

    clients_count = models.IntegerField(
        "Happy Clients",
        default=1
    )   

    hours_support = models.IntegerField(
        "Hours support",
        default=1
    )
    awards = models.IntegerField(
        "Awards"
    )
    def __str__(self,*args, **kwargs):
        return f"{self.id}{self.name}"
    
    def __unicode__(self, *args, **kwargs):
        return f"{self.id}{self.name}"

class Skill(models.Model):
    description = models.TextField(
            'description'
    )
    def __str__(self,*args, **kwargs):
        return f"{self.id}{self.description}"
    
    def __unicode__(self, *args, **kwargs):
        return f"{self.id}{self.description}"
    

class SkillData(models.Model):
    skills = models.ForeignKey(
        Skill,
        on_delete=models.SET_NULL,
        null = True,
        blank= True,
        related_name='skilldata'
    )

    language = models.CharField(
        'Language',
        max_length=20
    )

    knowledge = models.IntegerField(
        default=0
    )

    def __str__(self,*args, **kwargs):
        return f"{self.id}{self.language}"
    
    def __unicode__(self, *args, **kwargs):
        return f"{self.id}{self.language}"
