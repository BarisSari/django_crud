from django.conf.urls import url
from ..views import (FilmCategoryListView, FilmCategoryCreateView, FilmCategoryDetailView,
                     FilmCategoryUpdateView, FilmCategoryDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(FilmCategoryCreateView.as_view()),
        name="film_category_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(FilmCategoryUpdateView.as_view()),
        name="film_category_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(FilmCategoryDeleteView.as_view()),
        name="film_category_delete"),

    url(r'^(?P<pk>\d+)/$',
        FilmCategoryDetailView.as_view(),
        name="film_category_detail"),

    url(r'^$',
        FilmCategoryListView.as_view(),
        name="film_category_list"),
]
