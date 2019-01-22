from django.conf.urls import url
from ..views import (DjangoSessionListView, DjangoSessionCreateView, DjangoSessionDetailView,
                     DjangoSessionUpdateView, DjangoSessionDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(DjangoSessionCreateView.as_view()),
        name="django_session_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(DjangoSessionUpdateView.as_view()),
        name="django_session_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(DjangoSessionDeleteView.as_view()),
        name="django_session_delete"),

    url(r'^(?P<pk>\d+)/$',
        DjangoSessionDetailView.as_view(),
        name="django_session_detail"),

    url(r'^$',
        DjangoSessionListView.as_view(),
        name="django_session_list"),
]
