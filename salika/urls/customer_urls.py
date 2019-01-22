from django.conf.urls import url
from ..views import (CustomerListView, CustomerCreateView, CustomerDetailView,
                     CustomerUpdateView, CustomerDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(CustomerCreateView.as_view()),
        name="customer_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(CustomerUpdateView.as_view()),
        name="customer_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(CustomerDeleteView.as_view()),
        name="customer_delete"),

    url(r'^(?P<pk>\d+)/$',
        CustomerDetailView.as_view(),
        name="customer_detail"),

    url(r'^$',
        CustomerListView.as_view(),
        name="customer_list"),
]
