
from django.urls import path
from .views import test_response
from .views import wszystkie_filmy, nowy_film, edytuj_film, usun_film

urlpatterns = [
    path("filmy/", wszystkie_filmy, name='wszystkie_filmy'),
    path('test/', test_response),
    path("new/", nowy_film, name="nowy_film"),
    path('edytuj/<int:id>/', edytuj_film, name='edytuj_film'),
    path('usun/<int:id>/', usun_film, name="usun_film")

]
