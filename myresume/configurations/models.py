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

