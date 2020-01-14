from django.contrib import admin
from .models import Movie, Review, Aktor


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    # Filtrowanie elementów które mają być wyświetlone
    fields = ('name', 'description', 'year', 'relased', 'imdb_rating', 'photo')

    # wyświetlanie danych kolumn w postaci tabelek a po kliknięciu w dany "film" pokazuje się strona do edycji.
    list_display = ('name', 'year', 'description')

    # Filtrowanie "filmów" po ...
    list_filter = ('year', 'relased')

    # Wyszukiwanie po kategoriach
    search_fields = ('name', 'description', 'year', 'relased', 'imdb_rating')

#admin.site.register(ExtraInfo)
admin.site.register(Review)
admin.site.register(Aktor)
