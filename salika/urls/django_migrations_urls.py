from django.conf.urls import url
from ..views import (DjangoMigrationsListView, DjangoMigrationsCreateView, DjangoMigrationsDetailView,
                     DjangoMigrationsUpdateView, DjangoMigrationsDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(DjangoMigrationsCreateView.as_view()),
        name="django_migrations_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(DjangoMigrationsUpdateView.as_view()),
        name="django_migrations_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(DjangoMigrationsDeleteView.as_view()),
        name="django_migrations_delete"),

    url(r'^(?P<pk>\d+)/$',
        DjangoMigrationsDetailView.as_view(),
        name="django_migrations_detail"),

    url(r'^$',
        DjangoMigrationsListView.as_view(),
        name="django_migrations_list"),
]
