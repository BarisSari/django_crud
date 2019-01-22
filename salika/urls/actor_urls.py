from django.conf.urls import url
from ..views import (ActorListView, ActorCreateView, ActorDetailView,
                     ActorUpdateView, ActorDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(ActorCreateView.as_view()),
        name="actor_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(ActorUpdateView.as_view()),
        name="actor_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(ActorDeleteView.as_view()),
        name="actor_delete"),

    url(r'^(?P<pk>\d+)/$',
        ActorDetailView.as_view(),
        name="actor_detail"),

    url(r'^$',
        ActorListView.as_view(),
        name="actor_list"),
]
