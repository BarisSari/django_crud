from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Film
from ..forms import FilmForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class FilmListView(ListView):
    model = Film
    template_name = "salika/film_list.html"
    paginate_by = 20
    context_object_name = "film_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(FilmListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(FilmListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(FilmListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(FilmListView, self).get_queryset()

    def get_allow_empty(self):
        return super(FilmListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(FilmListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(FilmListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(FilmListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(FilmListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(FilmListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(FilmListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FilmListView, self).get_template_names()


class FilmDetailView(DetailView):
    model = Film
    template_name = "salika/film_detail.html"
    context_object_name = "film"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(FilmDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(FilmDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(FilmDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(FilmDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(FilmDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(FilmDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(FilmDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(FilmDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(FilmDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FilmDetailView, self).get_template_names()


class FilmCreateView(CreateView):
    model = Film
    form_class = FilmForm
    # fields = ['film_id', 'title', 'description', 'release_year', 'language', 'rental_duration', 'rental_rate', 'length', 'replacement_cost', 'rating', 'last_update', 'special_features', 'fulltext']
    template_name = "salika/film_create.html"
    success_url = reverse_lazy("film_list")

    def __init__(self, **kwargs):
        return super(FilmCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(FilmCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(FilmCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(FilmCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(FilmCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(FilmCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(FilmCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(FilmCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(FilmCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(FilmCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(FilmCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(FilmCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FilmCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:film_detail", args=(self.object.pk,))


class FilmUpdateView(UpdateView):
    model = Film
    form_class = FilmForm
    # fields = ['film_id', 'title', 'description', 'release_year', 'language', 'rental_duration', 'rental_rate', 'length', 'replacement_cost', 'rating', 'last_update', 'special_features', 'fulltext']
    template_name = "salika/film_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "film"

    def __init__(self, **kwargs):
        return super(FilmUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(FilmUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(FilmUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(FilmUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(FilmUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(FilmUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(FilmUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(FilmUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(FilmUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(FilmUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(FilmUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(FilmUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(FilmUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(FilmUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(FilmUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(FilmUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FilmUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:film_detail", args=(self.object.pk,))


class FilmDeleteView(DeleteView):
    model = Film
    template_name = "salika/film_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "film"

    def __init__(self, **kwargs):
        return super(FilmDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(FilmDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(FilmDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(FilmDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(FilmDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(FilmDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(FilmDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(FilmDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(FilmDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(FilmDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FilmDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:film_list")
