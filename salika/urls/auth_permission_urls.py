from django.conf.urls import url
from ..views import (AuthPermissionListView, AuthPermissionCreateView, AuthPermissionDetailView,
                     AuthPermissionUpdateView, AuthPermissionDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(AuthPermissionCreateView.as_view()),
        name="auth_permission_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(AuthPermissionUpdateView.as_view()),
        name="auth_permission_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(AuthPermissionDeleteView.as_view()),
        name="auth_permission_delete"),

    url(r'^(?P<pk>\d+)/$',
        AuthPermissionDetailView.as_view(),
        name="auth_permission_detail"),

    url(r'^$',
        AuthPermissionListView.as_view(),
        name="auth_permission_list"),
]
