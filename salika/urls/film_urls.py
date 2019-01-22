from django.conf.urls import url
from ..views import (FilmListView, FilmCreateView, FilmDetailView,
                     FilmUpdateView, FilmDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(FilmCreateView.as_view()),
        name="film_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(FilmUpdateView.as_view()),
        name="film_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(FilmDeleteView.as_view()),
        name="film_delete"),

    url(r'^(?P<pk>\d+)/$',
        FilmDetailView.as_view(),
        name="film_detail"),

    url(r'^$',
        FilmListView.as_view(),
        name="film_list"),
]
