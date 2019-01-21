from django.db import models
from django.forms import ModelForm


class Actor(models.Model):
    class Meta:
        db_table = 'actor'
        ordering = ['actor_id']

    actor_id = models.IntegerField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField(auto_now_add=True)
    # actor_id = models.ForeignKey(FilmActor, on_delete=models.CASCADE,
    #                              related_name='actor_id_test')

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class ActorForm(ModelForm):
    class Meta:
        model = Actor
        fields = ['actor_id', 'first_name', 'last_name']
        readonly_fields = ('last_update',)


class FilmActor(models.Model):
    class Meta:
        db_table = 'film_actor'
        ordering = ['actor_id']
        unique_together = ('actor_id', 'film_id',)

    actor_id = models.ForeignKey(Actor, on_delete=models.CASCADE,
                                 db_column='actor_id')
    # actor_id = models.SmallIntegerField()
    film_id = models.SmallIntegerField()
    last_update = models.DateTimeField(auto_now_add=True)
