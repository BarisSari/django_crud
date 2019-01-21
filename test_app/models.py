from django.db import models
from django.urls import reverse


class Actor(models.Model):
    actor_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    # last_update = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        return reverse('actor_edit', kwargs={'pk': self.actor_id})
