from django.conf.urls import url
from ..views import (DjangoContentTypeListView, DjangoContentTypeCreateView, DjangoContentTypeDetailView,
                     DjangoContentTypeUpdateView, DjangoContentTypeDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(DjangoContentTypeCreateView.as_view()),
        name="django_content_type_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(DjangoContentTypeUpdateView.as_view()),
        name="django_content_type_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(DjangoContentTypeDeleteView.as_view()),
        name="django_content_type_delete"),

    url(r'^(?P<pk>\d+)/$',
        DjangoContentTypeDetailView.as_view(),
        name="django_content_type_detail"),

    url(r'^$',
        DjangoContentTypeListView.as_view(),
        name="django_content_type_list"),
]
