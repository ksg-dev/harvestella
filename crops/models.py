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
    image = models.ImageField(upload_to="pics", null=True)
    buy = models.PositiveIntegerField()
    sell = models.PositiveIntegerField()
    reharvest = models.PositiveIntegerField(default=1)
    total_sell = models.PositiveIntegerField(blank=True)
    premium_sell = models.PositiveIntegerField(null=True)
    total_profit = models.PositiveIntegerField(blank=True)
    slug = models.SlugField(unique=True)
    grow_season = models.ManyToManyField(Seasons)
    biome = models.ForeignKey(Biome, on_delete=models.SET_NULL, null=True, related_name="biome")
            
    def save(self, *args, **kwargs):
        self.total_sell = self.sell * self.reharvest
        self.total_profit = self.total_sell - self.buy
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.crop_name} - Buy: {self.buy} - Sell: {self.sell} Total Profit: {self.total_profit}"

