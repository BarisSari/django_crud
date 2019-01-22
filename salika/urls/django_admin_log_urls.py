from django.conf.urls import url
from ..views import (DjangoAdminLogListView, DjangoAdminLogCreateView, DjangoAdminLogDetailView,
                     DjangoAdminLogUpdateView, DjangoAdminLogDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(DjangoAdminLogCreateView.as_view()),
        name="django_admin_log_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(DjangoAdminLogUpdateView.as_view()),
        name="django_admin_log_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(DjangoAdminLogDeleteView.as_view()),
        name="django_admin_log_delete"),

    url(r'^(?P<pk>\d+)/$',
        DjangoAdminLogDetailView.as_view(),
        name="django_admin_log_detail"),

    url(r'^$',
        DjangoAdminLogListView.as_view(),
        name="django_admin_log_list"),
]
