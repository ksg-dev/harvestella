from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView

from .models import Crop, Seasons, Biome

class StartingPageView(ListView):
    template_name = "crops/index.html"
    model = Crop
    context_object_name = "crops"

class AllCropsView(ListView):
    template_name = "crops/all-crops.html"
    model = Crop
    context_object_name = "all_crops"

class SingleCropView(View):
    def is_stored_item(self, request, crop_id):
        stored_items = request.session.get("stored_items")
        if stored_items is not None:
            is_saved_for_later = crop_id in stored_items
        else:
            is_saved_for_later = False
        
        return is_saved_for_later

    def get(self, request, slug):
        crop = Crop.objects.get(slug=slug)

        context = {
            "crop" : crop,
            "crop_seasons" : crop.grow_season.all(),
            "saved_for_later" : self.is_stored_item(request, crop.id)
        }

        return render(request, "crops/crop-detail.html", context)

class


