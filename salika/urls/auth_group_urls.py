from django.conf.urls import url
from ..views import (AuthGroupListView, AuthGroupCreateView, AuthGroupDetailView,
                     AuthGroupUpdateView, AuthGroupDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(AuthGroupCreateView.as_view()),
        name="auth_group_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(AuthGroupUpdateView.as_view()),
        name="auth_group_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(AuthGroupDeleteView.as_view()),
        name="auth_group_delete"),

    url(r'^(?P<pk>\d+)/$',
        AuthGroupDetailView.as_view(),
        name="auth_group_detail"),

    url(r'^$',
        AuthGroupListView.as_view(),
        name="auth_group_list"),
]
