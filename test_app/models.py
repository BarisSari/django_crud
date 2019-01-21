from django.db import models
from django.urls import reverse
from django.forms import ModelForm


class Actor(models.Model):
    class Meta:
        db_table = 'actor'
        ordering = ['actor_id']

    actor_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class ActorForm(ModelForm):
    class Meta:
        model = Actor
        fields = ['actor_id', 'first_name', 'last_name']
        readonly_fields = ('last_update',)
