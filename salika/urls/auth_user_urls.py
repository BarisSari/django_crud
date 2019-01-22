from django.conf.urls import url
from ..views import (AuthUserListView, AuthUserCreateView, AuthUserDetailView,
                     AuthUserUpdateView, AuthUserDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(AuthUserCreateView.as_view()),
        name="auth_user_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(AuthUserUpdateView.as_view()),
        name="auth_user_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(AuthUserDeleteView.as_view()),
        name="auth_user_delete"),

    url(r'^(?P<pk>\d+)/$',
        AuthUserDetailView.as_view(),
        name="auth_user_detail"),

    url(r'^$',
        AuthUserListView.as_view(),
        name="auth_user_list"),
]
