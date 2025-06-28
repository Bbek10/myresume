from django.contrib import admin
# imported configurations in self app admin
from .models import (Configurations)


# Register your models here.
@admin.register(Configurations)
class ConfigurationsModelAdmin(admin.ModelAdmin):
    pass

