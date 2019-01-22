from django.conf.urls import url
from ..views import (CityListView, CityCreateView, CityDetailView,
                     CityUpdateView, CityDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(CityCreateView.as_view()),
        name="city_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(CityUpdateView.as_view()),
        name="city_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(CityDeleteView.as_view()),
        name="city_delete"),

    url(r'^(?P<pk>\d+)/$',
        CityDetailView.as_view(),
        name="city_detail"),

    url(r'^$',
        CityListView.as_view(),
        name="city_list"),
]
