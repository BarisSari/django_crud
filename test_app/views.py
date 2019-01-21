from django.shortcuts import render, redirect, get_object_or_404
from test_app.models import Actor, ActorForm


def actor_list(request, template_name='test_app/actor_list.html'):
    actor = Actor.objects.all()
    data = {'object_list': actor}

    return render(request, template_name, data)


def actor_view(request, pk, template_name='test_app/actor_detail.html'):
    actor = get_object_or_404(Actor, pk=pk)
    return render(request, template_name, {'object': actor})


def actor_create(request, template_name='test_app/actor_form.html'):
    form = ActorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('actor_list')
    return render(request, template_name, {'form': form})


def actor_update(request, pk, template_name='test_app/actor_form.html'):
    actor = get_object_or_404(Actor, pk=pk)
    form = ActorForm(request.POST or None, instance=actor)
    if form.is_valid():
        form.save()
        return redirect('actor_list')
    return render(request, template_name, {'form': form})


def actor_delete(request, pk,
                 template_name='test_app/actor_confirm_delete.html'):
    actor = get_object_or_404(Actor, pk=pk)
    if request.method == 'POST':
        actor.delete()
        return redirect('actor_list')
    return render(request, template_name, {'object': actor})
