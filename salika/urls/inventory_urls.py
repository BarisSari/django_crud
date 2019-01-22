from django.conf.urls import url
from ..views import (InventoryListView, InventoryCreateView, InventoryDetailView,
                     InventoryUpdateView, InventoryDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(InventoryCreateView.as_view()),
        name="inventory_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(InventoryUpdateView.as_view()),
        name="inventory_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(InventoryDeleteView.as_view()),
        name="inventory_delete"),

    url(r'^(?P<pk>\d+)/$',
        InventoryDetailView.as_view(),
        name="inventory_detail"),

    url(r'^$',
        InventoryListView.as_view(),
        name="inventory_list"),
]
