from django.conf.urls import url
from ..views import (AuthUserUserPermissionsListView, AuthUserUserPermissionsCreateView, AuthUserUserPermissionsDetailView,
                     AuthUserUserPermissionsUpdateView, AuthUserUserPermissionsDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(AuthUserUserPermissionsCreateView.as_view()),
        name="auth_user_user_permissions_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(AuthUserUserPermissionsUpdateView.as_view()),
        name="auth_user_user_permissions_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(AuthUserUserPermissionsDeleteView.as_view()),
        name="auth_user_user_permissions_delete"),

    url(r'^(?P<pk>\d+)/$',
        AuthUserUserPermissionsDetailView.as_view(),
        name="auth_user_user_permissions_detail"),

    url(r'^$',
        AuthUserUserPermissionsListView.as_view(),
        name="auth_user_user_permissions_list"),
]
