from django.db import models


class Biome(models.Model):
    biome_name = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.biome_name}"



class Seasons(models.Model):
    season = models.CharField(max_length=10)
    
    def __str__(self):
        return self.season

    class Meta:
        verbose_name_plural = "Seasons"

class Crop(models.Model):
    crop_name = models.CharField(max_length=50)
    buy = models.IntegerField()
    sell = models.IntegerField()
    image_name = models.CharField(max_length=100, default="static/crops/images/space.jpg")
    slug = models.SlugField(unique=True)
    grow_season = models.ManyToManyField(Seasons)
    biome = models.ForeignKey(Biome, on_delete=models.SET_NULL, null=True, related_name="biome")
            
    def __str__(self):
        return f"{self.crop_name} - {self.buy} - {self.sell}"

