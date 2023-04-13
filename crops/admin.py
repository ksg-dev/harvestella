from django.contrib import admin
from .models import Crop, Seasons, Biome

class CropAdmin(admin.ModelAdmin):
    list_display = ("crop_name", "buy", "sell", "biome")
    prepopulated_fields = {"slug":("crop_name", )}

class SeasonsAdmin(admin.ModelAdmin):
    list_display = ("")

admin.site.register(Crop, CropAdmin)
admin.site.register(Seasons)
admin.site.register(Biome)
