from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(default="")
    year = models.IntegerField(null=True, blank=True)
    relased = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(null=True, blank=True, max_digits=10, decimal_places=7)
    photo = models.ImageField(null=True, blank=True, upload_to='Filmy')

    def __str__(self):
        return self.name_width_year()

    def name_width_year(self):
        return str(self.name) + " (" + str(self.year) + ")"