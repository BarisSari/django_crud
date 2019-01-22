from django.conf.urls import url
from ..views import (StaffListView, StaffCreateView, StaffDetailView,
                     StaffUpdateView, StaffDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(StaffCreateView.as_view()),
        name="staff_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(StaffUpdateView.as_view()),
        name="staff_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(StaffDeleteView.as_view()),
        name="staff_delete"),

    url(r'^(?P<pk>\d+)/$',
        StaffDetailView.as_view(),
        name="staff_detail"),

    url(r'^$',
        StaffListView.as_view(),
        name="staff_list"),
]
