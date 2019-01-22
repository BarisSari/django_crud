from django.conf.urls import url
from ..views import (CountryListView, CountryCreateView, CountryDetailView,
                     CountryUpdateView, CountryDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(CountryCreateView.as_view()),
        name="country_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(CountryUpdateView.as_view()),
        name="country_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(CountryDeleteView.as_view()),
        name="country_delete"),

    url(r'^(?P<pk>\d+)/$',
        CountryDetailView.as_view(),
        name="country_detail"),

    url(r'^$',
        CountryListView.as_view(),
        name="country_list"),
]
