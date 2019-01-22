from django.conf.urls import url
from ..views import (PaymentListView, PaymentCreateView, PaymentDetailView,
                     PaymentUpdateView, PaymentDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(PaymentCreateView.as_view()),
        name="payment_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(PaymentUpdateView.as_view()),
        name="payment_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(PaymentDeleteView.as_view()),
        name="payment_delete"),

    url(r'^(?P<pk>\d+)/$',
        PaymentDetailView.as_view(),
        name="payment_detail"),

    url(r'^$',
        PaymentListView.as_view(),
        name="payment_list"),
]
