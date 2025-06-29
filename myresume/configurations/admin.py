from django.contrib import admin
# imported configurations in self app admin
from .models import (Configurations, Stats, Skill, SkillData)


# Register your models here.
@admin.register(Configurations)
class ConfigurationsModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Stats)
class StatsModelAdmin(admin.ModelAdmin):
    pass


class SkillDataTabularInline(admin.TabularInline):
    model = SkillData

class SkillModelAdmin (admin.ModelAdmin):
    inlines = [SkillDataTabularInline]

    class Meta:
        model = Skill

admin.site.register(Skill, SkillModelAdmin)     