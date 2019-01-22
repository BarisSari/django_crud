from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import DjangoMigrations
from ..forms import DjangoMigrationsForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class DjangoMigrationsListView(ListView):
    model = DjangoMigrations
    template_name = "salika/django_migrations_list.html"
    paginate_by = 20
    context_object_name = "django_migrations_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(DjangoMigrationsListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DjangoMigrationsListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DjangoMigrationsListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(DjangoMigrationsListView, self).get_queryset()

    def get_allow_empty(self):
        return super(DjangoMigrationsListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(DjangoMigrationsListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(DjangoMigrationsListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(DjangoMigrationsListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(DjangoMigrationsListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(DjangoMigrationsListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(DjangoMigrationsListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DjangoMigrationsListView, self).get_template_names()


class DjangoMigrationsDetailView(DetailView):
    model = DjangoMigrations
    template_name = "salika/django_migrations_detail.html"
    context_object_name = "django_migrations"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(DjangoMigrationsDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DjangoMigrationsDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DjangoMigrationsDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DjangoMigrationsDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(DjangoMigrationsDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(DjangoMigrationsDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(DjangoMigrationsDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DjangoMigrationsDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DjangoMigrationsDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DjangoMigrationsDetailView, self).get_template_names()


class DjangoMigrationsCreateView(CreateView):
    model = DjangoMigrations
    form_class = DjangoMigrationsForm
    # fields = ['app', 'name', 'applied']
    template_name = "salika/django_migrations_create.html"
    success_url = reverse_lazy("django_migrations_list")

    def __init__(self, **kwargs):
        return super(DjangoMigrationsCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(DjangoMigrationsCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DjangoMigrationsCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(DjangoMigrationsCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(DjangoMigrationsCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(DjangoMigrationsCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(DjangoMigrationsCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(DjangoMigrationsCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(DjangoMigrationsCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(DjangoMigrationsCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(DjangoMigrationsCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(DjangoMigrationsCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DjangoMigrationsCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:django_migrations_detail", args=(self.object.pk,))


class DjangoMigrationsUpdateView(UpdateView):
    model = DjangoMigrations
    form_class = DjangoMigrationsForm
    # fields = ['app', 'name', 'applied']
    template_name = "salika/django_migrations_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "django_migrations"

    def __init__(self, **kwargs):
        return super(DjangoMigrationsUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DjangoMigrationsUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DjangoMigrationsUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(DjangoMigrationsUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DjangoMigrationsUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(DjangoMigrationsUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(DjangoMigrationsUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(DjangoMigrationsUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(DjangoMigrationsUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(DjangoMigrationsUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(DjangoMigrationsUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(DjangoMigrationsUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(DjangoMigrationsUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(DjangoMigrationsUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DjangoMigrationsUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DjangoMigrationsUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DjangoMigrationsUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:django_migrations_detail", args=(self.object.pk,))


class DjangoMigrationsDeleteView(DeleteView):
    model = DjangoMigrations
    template_name = "salika/django_migrations_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "django_migrations"

    def __init__(self, **kwargs):
        return super(DjangoMigrationsDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DjangoMigrationsDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(DjangoMigrationsDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(DjangoMigrationsDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DjangoMigrationsDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(DjangoMigrationsDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(DjangoMigrationsDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(DjangoMigrationsDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DjangoMigrationsDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DjangoMigrationsDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DjangoMigrationsDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:django_migrations_list")
