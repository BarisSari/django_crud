from django.conf.urls import url
from ..views import (AuthGroupPermissionsListView, AuthGroupPermissionsCreateView, AuthGroupPermissionsDetailView,
                     AuthGroupPermissionsUpdateView, AuthGroupPermissionsDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(AuthGroupPermissionsCreateView.as_view()),
        name="auth_group_permissions_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(AuthGroupPermissionsUpdateView.as_view()),
        name="auth_group_permissions_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(AuthGroupPermissionsDeleteView.as_view()),
        name="auth_group_permissions_delete"),

    url(r'^(?P<pk>\d+)/$',
        AuthGroupPermissionsDetailView.as_view(),
        name="auth_group_permissions_detail"),

    url(r'^$',
        AuthGroupPermissionsListView.as_view(),
        name="auth_group_permissions_list"),
]
