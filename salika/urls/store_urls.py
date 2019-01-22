from django.conf.urls import url
from ..views import (StoreListView, StoreCreateView, StoreDetailView,
                     StoreUpdateView, StoreDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(StoreCreateView.as_view()),
        name="store_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(StoreUpdateView.as_view()),
        name="store_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(StoreDeleteView.as_view()),
        name="store_delete"),

    url(r'^(?P<pk>\d+)/$',
        StoreDetailView.as_view(),
        name="store_detail"),

    url(r'^$',
        StoreListView.as_view(),
        name="store_list"),
]
