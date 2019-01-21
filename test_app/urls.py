from django.urls import path

from . import views

urlpatterns = [
    path('', views.actor_list, name='actor_list'),
    path('new', views.actor_create, name='actor_new'),
    path('view/<int:pk>', views.actor_view, name='actor_view'),
    path('edit/<int:pk>', views.actor_update, name='actor_edit'),
    path('delete/<int:pk>', views.actor_delete, name='actor_delete'),
]
