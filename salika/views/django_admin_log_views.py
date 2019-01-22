from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import DjangoAdminLog
from ..forms import DjangoAdminLogForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class DjangoAdminLogListView(ListView):
    model = DjangoAdminLog
    template_name = "salika/django_admin_log_list.html"
    paginate_by = 20
    context_object_name = "django_admin_log_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(DjangoAdminLogListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DjangoAdminLogListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DjangoAdminLogListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(DjangoAdminLogListView, self).get_queryset()

    def get_allow_empty(self):
        return super(DjangoAdminLogListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(DjangoAdminLogListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(DjangoAdminLogListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(DjangoAdminLogListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(DjangoAdminLogListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(DjangoAdminLogListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(DjangoAdminLogListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DjangoAdminLogListView, self).get_template_names()


class DjangoAdminLogDetailView(DetailView):
    model = DjangoAdminLog
    template_name = "salika/django_admin_log_detail.html"
    context_object_name = "django_admin_log"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(DjangoAdminLogDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DjangoAdminLogDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DjangoAdminLogDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DjangoAdminLogDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(DjangoAdminLogDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(DjangoAdminLogDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(DjangoAdminLogDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DjangoAdminLogDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DjangoAdminLogDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DjangoAdminLogDetailView, self).get_template_names()


class DjangoAdminLogCreateView(CreateView):
    model = DjangoAdminLog
    form_class = DjangoAdminLogForm
    # fields = ['action_time', 'object_id', 'object_repr', 'action_flag', 'change_message', 'content_type', 'user']
    template_name = "salika/django_admin_log_create.html"
    success_url = reverse_lazy("django_admin_log_list")

    def __init__(self, **kwargs):
        return super(DjangoAdminLogCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(DjangoAdminLogCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DjangoAdminLogCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(DjangoAdminLogCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(DjangoAdminLogCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(DjangoAdminLogCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(DjangoAdminLogCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(DjangoAdminLogCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(DjangoAdminLogCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(DjangoAdminLogCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(DjangoAdminLogCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(DjangoAdminLogCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DjangoAdminLogCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:django_admin_log_detail", args=(self.object.pk,))


class DjangoAdminLogUpdateView(UpdateView):
    model = DjangoAdminLog
    form_class = DjangoAdminLogForm
    # fields = ['action_time', 'object_id', 'object_repr', 'action_flag', 'change_message', 'content_type', 'user']
    template_name = "salika/django_admin_log_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "django_admin_log"

    def __init__(self, **kwargs):
        return super(DjangoAdminLogUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DjangoAdminLogUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DjangoAdminLogUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(DjangoAdminLogUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DjangoAdminLogUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(DjangoAdminLogUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(DjangoAdminLogUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(DjangoAdminLogUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(DjangoAdminLogUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(DjangoAdminLogUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(DjangoAdminLogUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(DjangoAdminLogUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(DjangoAdminLogUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(DjangoAdminLogUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DjangoAdminLogUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DjangoAdminLogUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DjangoAdminLogUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:django_admin_log_detail", args=(self.object.pk,))


class DjangoAdminLogDeleteView(DeleteView):
    model = DjangoAdminLog
    template_name = "salika/django_admin_log_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "django_admin_log"

    def __init__(self, **kwargs):
        return super(DjangoAdminLogDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DjangoAdminLogDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(DjangoAdminLogDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(DjangoAdminLogDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DjangoAdminLogDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(DjangoAdminLogDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(DjangoAdminLogDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(DjangoAdminLogDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DjangoAdminLogDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DjangoAdminLogDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DjangoAdminLogDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:django_admin_log_list")
