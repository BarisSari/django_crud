from django.conf.urls import url
from ..views import (AddressListView, AddressCreateView, AddressDetailView,
                     AddressUpdateView, AddressDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(AddressCreateView.as_view()),
        name="address_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(AddressUpdateView.as_view()),
        name="address_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(AddressDeleteView.as_view()),
        name="address_delete"),

    url(r'^(?P<pk>\d+)/$',
        AddressDetailView.as_view(),
        name="address_detail"),

    url(r'^$',
        AddressListView.as_view(),
        name="address_list"),
]
