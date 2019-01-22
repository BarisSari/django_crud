from django.conf.urls import url
from ..views import (LanguageListView, LanguageCreateView, LanguageDetailView,
                     LanguageUpdateView, LanguageDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(LanguageCreateView.as_view()),
        name="language_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(LanguageUpdateView.as_view()),
        name="language_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(LanguageDeleteView.as_view()),
        name="language_delete"),

    url(r'^(?P<pk>\d+)/$',
        LanguageDetailView.as_view(),
        name="language_detail"),

    url(r'^$',
        LanguageListView.as_view(),
        name="language_list"),
]
