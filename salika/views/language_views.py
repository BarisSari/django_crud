from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Language
from ..forms import LanguageForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class LanguageListView(ListView):
    model = Language
    template_name = "salika/language_list.html"
    paginate_by = 20
    context_object_name = "language_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(LanguageListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(LanguageListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(LanguageListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(LanguageListView, self).get_queryset()

    def get_allow_empty(self):
        return super(LanguageListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(LanguageListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(LanguageListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(LanguageListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(LanguageListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(LanguageListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(LanguageListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LanguageListView, self).get_template_names()


class LanguageDetailView(DetailView):
    model = Language
    template_name = "salika/language_detail.html"
    context_object_name = "language"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(LanguageDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(LanguageDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(LanguageDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(LanguageDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(LanguageDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(LanguageDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(LanguageDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(LanguageDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(LanguageDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LanguageDetailView, self).get_template_names()


class LanguageCreateView(CreateView):
    model = Language
    form_class = LanguageForm
    # fields = ['language_id', 'name', 'last_update']
    template_name = "salika/language_create.html"
    success_url = reverse_lazy("language_list")

    def __init__(self, **kwargs):
        return super(LanguageCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(LanguageCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(LanguageCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(LanguageCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(LanguageCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(LanguageCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(LanguageCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(LanguageCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(LanguageCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(LanguageCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(LanguageCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(LanguageCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LanguageCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:language_detail", args=(self.object.pk,))


class LanguageUpdateView(UpdateView):
    model = Language
    form_class = LanguageForm
    # fields = ['language_id', 'name', 'last_update']
    template_name = "salika/language_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "language"

    def __init__(self, **kwargs):
        return super(LanguageUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(LanguageUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(LanguageUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(LanguageUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(LanguageUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(LanguageUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(LanguageUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(LanguageUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(LanguageUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(LanguageUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(LanguageUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(LanguageUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(LanguageUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(LanguageUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(LanguageUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(LanguageUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LanguageUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:language_detail", args=(self.object.pk,))


class LanguageDeleteView(DeleteView):
    model = Language
    template_name = "salika/language_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "language"

    def __init__(self, **kwargs):
        return super(LanguageDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(LanguageDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(LanguageDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(LanguageDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(LanguageDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(LanguageDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(LanguageDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(LanguageDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(LanguageDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(LanguageDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(LanguageDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:language_list")
