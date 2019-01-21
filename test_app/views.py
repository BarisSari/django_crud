from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from test_app.models import Actor
import psycopg2


class ActorForm(ModelForm):
    class Meta:
        model = Actor
        fields = ['actor_id', 'first_name', 'last_name']


def actor_list(request, template_name='actor/actor_list.html'):
    actor = Actor.objects.all()
    # data = {'object_list': actor}
    connection = psycopg2.connect(database='postgres', user='baris',
                                  password='4865')
    cur = connection.cursor()
    cur.execute("SELECT * FROM actor")
    records = cur.fetchall()

    print(records)

    # data = {"id": 1, "first_name": "test", "second_name": "deneme",
    #         "update": "2018"}
    print("123")
    return render(request, template_name, "x")


def actor_view(request, pk, template_name='actor/actor_detail.html'):
    actor = get_object_or_404(Actor, pk=pk)
    return render(request, template_name, {'object': actor})


def actor_create(request, template_name='actor/actor_form.html'):
    form = ActorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('actor_list')
    return render(request, template_name, {'form': form})


def actor_update(request, pk, template_name='actor/actor_form.html'):
    actor = get_object_or_404(Actor, pk=pk)
    form = ActorForm(request.POST or None, instance=actor)
    if form.is_valid():
        form.save()
        return redirect('actor_list')
    return render(request, template_name, {'form': form})


def actor_delete(request, pk, template_name='actor/actor_confirm_delete.html'):
    actor = get_object_or_404(Actor, pk=pk)
    if request.method == 'POST':
        actor.delete()
        return redirect('actor_list')
    return render(request, template_name, {'object': actor})
