from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Actor
from ..forms import ActorForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class ActorListView(ListView):
    model = Actor
    template_name = "salika/actor_list.html"
    paginate_by = 20
    context_object_name = "actor_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(ActorListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ActorListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ActorListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(ActorListView, self).get_queryset()

    def get_allow_empty(self):
        return super(ActorListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(ActorListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(ActorListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(ActorListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(ActorListView, self).paginate_queryset(queryset,
                                                            page_size)

    def get_paginator(self, queryset, per_page, orphans=0,
                      allow_empty_first_page=True):
        return super(ActorListView, self).get_paginator(queryset, per_page,
                                                        orphans=0,
                                                        allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(ActorListView, self).render_to_response(context,
                                                             **response_kwargs)

    def get_template_names(self):
        return super(ActorListView, self).get_template_names()


class ActorDetailView(DetailView):
    model = Actor
    template_name = "salika/actor_detail.html"
    context_object_name = "actor"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(ActorDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ActorDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ActorDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ActorDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(ActorDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(ActorDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(ActorDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ActorDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ActorDetailView, self).render_to_response(context,
                                                               **response_kwargs)

    def get_template_names(self):
        return super(ActorDetailView, self).get_template_names()


class ActorCreateView(CreateView):
    model = Actor
    form_class = ActorForm
    # fields = ['actor_id', 'first_name', 'last_name', 'last_update']
    template_name = "salika/actor_create.html"
    success_url = reverse_lazy("actor_list")

    def __init__(self, **kwargs):
        return super(ActorCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(ActorCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ActorCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(ActorCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(ActorCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(ActorCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(ActorCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(ActorCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(ActorCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(ActorCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(ActorCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(ActorCreateView, self).render_to_response(context,
                                                               **response_kwargs)

    def get_template_names(self):
        return super(ActorCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:actor_detail", args=(self.object.pk,))


class ActorUpdateView(UpdateView):
    model = Actor
    form_class = ActorForm
    # fields = ['actor_id', 'first_name', 'last_name', 'last_update']
    template_name = "salika/actor_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "actor"

    def __init__(self, **kwargs):
        return super(ActorUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ActorUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ActorUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(ActorUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ActorUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(ActorUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(ActorUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(ActorUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(ActorUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(ActorUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(ActorUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(ActorUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(ActorUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(ActorUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ActorUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ActorUpdateView, self).render_to_response(context,
                                                               **response_kwargs)

    def get_template_names(self):
        return super(ActorUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:actor_detail", args=(self.object.pk,))


class ActorDeleteView(DeleteView):
    model = Actor
    template_name = "salika/actor_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "actor"

    def __init__(self, **kwargs):
        return super(ActorDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ActorDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(ActorDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(ActorDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ActorDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(ActorDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(ActorDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(ActorDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ActorDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ActorDeleteView, self).render_to_response(context,
                                                               **response_kwargs)

    def get_template_names(self):
        return super(ActorDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:actor_list")
