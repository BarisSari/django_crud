from django.conf.urls import url
from ..views import (AuthUserGroupsListView, AuthUserGroupsCreateView, AuthUserGroupsDetailView,
                     AuthUserGroupsUpdateView, AuthUserGroupsDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(AuthUserGroupsCreateView.as_view()),
        name="auth_user_groups_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(AuthUserGroupsUpdateView.as_view()),
        name="auth_user_groups_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(AuthUserGroupsDeleteView.as_view()),
        name="auth_user_groups_delete"),

    url(r'^(?P<pk>\d+)/$',
        AuthUserGroupsDetailView.as_view(),
        name="auth_user_groups_detail"),

    url(r'^$',
        AuthUserGroupsListView.as_view(),
        name="auth_user_groups_list"),
]
