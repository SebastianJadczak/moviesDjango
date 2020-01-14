from django.db import models


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


class Review(models.Model):
    text = models.CharField(default='', blank=True, max_length=120)
    stars = models.IntegerField(default=5)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Aktor(models.Model):
    imie = models.CharField(max_length=128)
    nazwisko = models.CharField(max_length=120)
    filmy = models.ManyToManyField(Movie)

    def __str__(self):
        return self.show_name_actor()

    def show_name_actor(self):
        return str(self.imie) + " " + str(self.nazwisko)


