from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import City
from ..forms import CityForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class CityListView(ListView):
    model = City
    template_name = "salika/city_list.html"
    paginate_by = 20
    context_object_name = "city_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(CityListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CityListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CityListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(CityListView, self).get_queryset()

    def get_allow_empty(self):
        return super(CityListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(CityListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(CityListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(CityListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(CityListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(CityListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(CityListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CityListView, self).get_template_names()


class CityDetailView(DetailView):
    model = City
    template_name = "salika/city_detail.html"
    context_object_name = "city"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(CityDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CityDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CityDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CityDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(CityDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(CityDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CityDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CityDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CityDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CityDetailView, self).get_template_names()


class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    # fields = ['city_id', 'city', 'country', 'last_update']
    template_name = "salika/city_create.html"
    success_url = reverse_lazy("city_list")

    def __init__(self, **kwargs):
        return super(CityCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(CityCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CityCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CityCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(CityCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CityCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CityCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CityCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(CityCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CityCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CityCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(CityCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CityCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:city_detail", args=(self.object.pk,))


class CityUpdateView(UpdateView):
    model = City
    form_class = CityForm
    # fields = ['city_id', 'city', 'country', 'last_update']
    template_name = "salika/city_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "city"

    def __init__(self, **kwargs):
        return super(CityUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CityUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CityUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CityUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CityUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(CityUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(CityUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(CityUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CityUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CityUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CityUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(CityUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CityUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CityUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CityUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CityUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CityUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:city_detail", args=(self.object.pk,))


class CityDeleteView(DeleteView):
    model = City
    template_name = "salika/city_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "city"

    def __init__(self, **kwargs):
        return super(CityDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CityDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(CityDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(CityDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CityDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(CityDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(CityDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CityDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CityDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CityDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CityDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:city_list")
