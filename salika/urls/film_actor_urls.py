from django.conf.urls import url
from ..views import (FilmActorListView, FilmActorCreateView, FilmActorDetailView,
                     FilmActorUpdateView, FilmActorDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(FilmActorCreateView.as_view()),
        name="film_actor_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(FilmActorUpdateView.as_view()),
        name="film_actor_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(FilmActorDeleteView.as_view()),
        name="film_actor_delete"),

    url(r'^(?P<pk>\d+)/$',
        FilmActorDetailView.as_view(),
        name="film_actor_detail"),

    url(r'^$',
        FilmActorListView.as_view(),
        name="film_actor_list"),
]
