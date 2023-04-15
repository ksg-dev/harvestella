from django.db import models

class CSV(models.Model):
    file_name = models.FileField(upload_to="pics/", max_length=100)
    uploaded = models.DateField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return "File id: {}".format(self.id)
