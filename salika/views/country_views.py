from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Country
from ..forms import CountryForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class CountryListView(ListView):
    model = Country
    template_name = "salika/country_list.html"
    paginate_by = 20
    context_object_name = "country_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(CountryListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CountryListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CountryListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(CountryListView, self).get_queryset()

    def get_allow_empty(self):
        return super(CountryListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(CountryListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(CountryListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(CountryListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(CountryListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(CountryListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(CountryListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CountryListView, self).get_template_names()


class CountryDetailView(DetailView):
    model = Country
    template_name = "salika/country_detail.html"
    context_object_name = "country"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(CountryDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CountryDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CountryDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CountryDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(CountryDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(CountryDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CountryDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CountryDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CountryDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CountryDetailView, self).get_template_names()


class CountryCreateView(CreateView):
    model = Country
    form_class = CountryForm
    # fields = ['country_id', 'country', 'last_update']
    template_name = "salika/country_create.html"
    success_url = reverse_lazy("country_list")

    def __init__(self, **kwargs):
        return super(CountryCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(CountryCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CountryCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CountryCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(CountryCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CountryCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CountryCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CountryCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(CountryCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CountryCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CountryCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(CountryCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CountryCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:country_detail", args=(self.object.pk,))


class CountryUpdateView(UpdateView):
    model = Country
    form_class = CountryForm
    # fields = ['country_id', 'country', 'last_update']
    template_name = "salika/country_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "country"

    def __init__(self, **kwargs):
        return super(CountryUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CountryUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CountryUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CountryUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CountryUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(CountryUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(CountryUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(CountryUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CountryUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CountryUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CountryUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(CountryUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CountryUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CountryUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CountryUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CountryUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CountryUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:country_detail", args=(self.object.pk,))


class CountryDeleteView(DeleteView):
    model = Country
    template_name = "salika/country_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "country"

    def __init__(self, **kwargs):
        return super(CountryDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CountryDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(CountryDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(CountryDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CountryDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(CountryDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(CountryDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CountryDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CountryDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CountryDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CountryDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:country_list")
