from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import DjangoSession
from ..forms import DjangoSessionForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class DjangoSessionListView(ListView):
    model = DjangoSession
    template_name = "salika/django_session_list.html"
    paginate_by = 20
    context_object_name = "django_session_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(DjangoSessionListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DjangoSessionListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DjangoSessionListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(DjangoSessionListView, self).get_queryset()

    def get_allow_empty(self):
        return super(DjangoSessionListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(DjangoSessionListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(DjangoSessionListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(DjangoSessionListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(DjangoSessionListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(DjangoSessionListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(DjangoSessionListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DjangoSessionListView, self).get_template_names()


class DjangoSessionDetailView(DetailView):
    model = DjangoSession
    template_name = "salika/django_session_detail.html"
    context_object_name = "django_session"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(DjangoSessionDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DjangoSessionDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DjangoSessionDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DjangoSessionDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(DjangoSessionDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(DjangoSessionDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(DjangoSessionDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DjangoSessionDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DjangoSessionDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DjangoSessionDetailView, self).get_template_names()


class DjangoSessionCreateView(CreateView):
    model = DjangoSession
    form_class = DjangoSessionForm
    # fields = ['session_key', 'session_data', 'expire_date']
    template_name = "salika/django_session_create.html"
    success_url = reverse_lazy("django_session_list")

    def __init__(self, **kwargs):
        return super(DjangoSessionCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(DjangoSessionCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DjangoSessionCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(DjangoSessionCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(DjangoSessionCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(DjangoSessionCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(DjangoSessionCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(DjangoSessionCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(DjangoSessionCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(DjangoSessionCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(DjangoSessionCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(DjangoSessionCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DjangoSessionCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:django_session_detail", args=(self.object.pk,))


class DjangoSessionUpdateView(UpdateView):
    model = DjangoSession
    form_class = DjangoSessionForm
    # fields = ['session_key', 'session_data', 'expire_date']
    template_name = "salika/django_session_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "django_session"

    def __init__(self, **kwargs):
        return super(DjangoSessionUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DjangoSessionUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DjangoSessionUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(DjangoSessionUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DjangoSessionUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(DjangoSessionUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(DjangoSessionUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(DjangoSessionUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(DjangoSessionUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(DjangoSessionUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(DjangoSessionUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(DjangoSessionUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(DjangoSessionUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(DjangoSessionUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DjangoSessionUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DjangoSessionUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DjangoSessionUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:django_session_detail", args=(self.object.pk,))


class DjangoSessionDeleteView(DeleteView):
    model = DjangoSession
    template_name = "salika/django_session_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "django_session"

    def __init__(self, **kwargs):
        return super(DjangoSessionDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DjangoSessionDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(DjangoSessionDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(DjangoSessionDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DjangoSessionDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(DjangoSessionDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(DjangoSessionDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(DjangoSessionDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DjangoSessionDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DjangoSessionDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DjangoSessionDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:django_session_list")
