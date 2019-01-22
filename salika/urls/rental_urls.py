from django.conf.urls import url
from ..views import (RentalListView, RentalCreateView, RentalDetailView,
                     RentalUpdateView, RentalDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(RentalCreateView.as_view()),
        name="rental_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(RentalUpdateView.as_view()),
        name="rental_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(RentalDeleteView.as_view()),
        name="rental_delete"),

    url(r'^(?P<pk>\d+)/$',
        RentalDetailView.as_view(),
        name="rental_detail"),

    url(r'^$',
        RentalListView.as_view(),
        name="rental_list"),
]
