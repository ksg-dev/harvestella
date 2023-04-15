from django.shortcuts import render
from .forms import CSVForm
from .models import CSV 
import csv
from crops.models import Crop, Biome, Seasons

def upload_file_view(request):
    form = CSVForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CSVForm()

        obj = CSV.objects.get(activated=False)
        with open(obj.file_name.path, "r") as f:
            reader = csv.reader(f)

            for row in reader:
                biome, _ = Biome.objects.get_or_create(biome_name=row[1])
                Crop.objects.get_or_create(
                    biome = biome,
                    crop_name = row[0],
                    buy = int(row[2]),
                    sell = int(row[3]),
                    reharvest = int(row[5]),
                    premium_sell = int(row[7]))
                
        obj.activated=True
        obj.save()

    context = {
        "form" : form,
    }
    
    return render(request, "files/upload.html", context)
                

