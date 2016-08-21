from django.contrib import admin
from app import models


@admin.register(models.Site)
class SiteAdmin(admin.ModelAdmin):
    pass


@admin.register(models.DataEntry)
class DataEntryAdmin(admin.ModelAdmin):
    pass
