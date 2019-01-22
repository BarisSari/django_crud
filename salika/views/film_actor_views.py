from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import FilmActor
from ..forms import FilmActorForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class FilmActorListView(ListView):
    model = FilmActor
    template_name = "salika/film_actor_list.html"
    paginate_by = 20
    context_object_name = "film_actor_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(FilmActorListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(FilmActorListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(FilmActorListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(FilmActorListView, self).get_queryset()

    def get_allow_empty(self):
        return super(FilmActorListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(FilmActorListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(FilmActorListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(FilmActorListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(FilmActorListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(FilmActorListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(FilmActorListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FilmActorListView, self).get_template_names()


class FilmActorDetailView(DetailView):
    model = FilmActor
    template_name = "salika/film_actor_detail.html"
    context_object_name = "film_actor"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(FilmActorDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(FilmActorDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(FilmActorDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(FilmActorDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(FilmActorDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(FilmActorDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(FilmActorDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(FilmActorDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(FilmActorDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FilmActorDetailView, self).get_template_names()


class FilmActorCreateView(CreateView):
    model = FilmActor
    form_class = FilmActorForm
    # fields = ['actor', 'film', 'last_update']
    template_name = "salika/film_actor_create.html"
    success_url = reverse_lazy("film_actor_list")

    def __init__(self, **kwargs):
        return super(FilmActorCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(FilmActorCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(FilmActorCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(FilmActorCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(FilmActorCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(FilmActorCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(FilmActorCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(FilmActorCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(FilmActorCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(FilmActorCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(FilmActorCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(FilmActorCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FilmActorCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:film_actor_detail", args=(self.object.pk,))


class FilmActorUpdateView(UpdateView):
    model = FilmActor
    form_class = FilmActorForm
    # fields = ['actor', 'film', 'last_update']
    template_name = "salika/film_actor_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "film_actor"

    def __init__(self, **kwargs):
        return super(FilmActorUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(FilmActorUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(FilmActorUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(FilmActorUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(FilmActorUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(FilmActorUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(FilmActorUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(FilmActorUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(FilmActorUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(FilmActorUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(FilmActorUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(FilmActorUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(FilmActorUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(FilmActorUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(FilmActorUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(FilmActorUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FilmActorUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:film_actor_detail", args=(self.object.pk,))


class FilmActorDeleteView(DeleteView):
    model = FilmActor
    template_name = "salika/film_actor_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "film_actor"

    def __init__(self, **kwargs):
        return super(FilmActorDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(FilmActorDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(FilmActorDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(FilmActorDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(FilmActorDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(FilmActorDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(FilmActorDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(FilmActorDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(FilmActorDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(FilmActorDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FilmActorDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:film_actor_list")
