from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import AuthPermission
from ..forms import AuthPermissionForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class AuthPermissionListView(ListView):
    model = AuthPermission
    template_name = "salika/auth_permission_list.html"
    paginate_by = 20
    context_object_name = "auth_permission_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(AuthPermissionListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AuthPermissionListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AuthPermissionListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(AuthPermissionListView, self).get_queryset()

    def get_allow_empty(self):
        return super(AuthPermissionListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(AuthPermissionListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(AuthPermissionListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(AuthPermissionListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(AuthPermissionListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(AuthPermissionListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(AuthPermissionListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthPermissionListView, self).get_template_names()


class AuthPermissionDetailView(DetailView):
    model = AuthPermission
    template_name = "salika/auth_permission_detail.html"
    context_object_name = "auth_permission"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(AuthPermissionDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AuthPermissionDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AuthPermissionDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AuthPermissionDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(AuthPermissionDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(AuthPermissionDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(AuthPermissionDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AuthPermissionDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AuthPermissionDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthPermissionDetailView, self).get_template_names()


class AuthPermissionCreateView(CreateView):
    model = AuthPermission
    form_class = AuthPermissionForm
    # fields = ['name', 'content_type', 'codename']
    template_name = "salika/auth_permission_create.html"
    success_url = reverse_lazy("auth_permission_list")

    def __init__(self, **kwargs):
        return super(AuthPermissionCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(AuthPermissionCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AuthPermissionCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(AuthPermissionCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(AuthPermissionCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(AuthPermissionCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(AuthPermissionCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(AuthPermissionCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(AuthPermissionCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(AuthPermissionCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(AuthPermissionCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(AuthPermissionCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthPermissionCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:auth_permission_detail", args=(self.object.pk,))


class AuthPermissionUpdateView(UpdateView):
    model = AuthPermission
    form_class = AuthPermissionForm
    # fields = ['name', 'content_type', 'codename']
    template_name = "salika/auth_permission_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "auth_permission"

    def __init__(self, **kwargs):
        return super(AuthPermissionUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AuthPermissionUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AuthPermissionUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(AuthPermissionUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AuthPermissionUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(AuthPermissionUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(AuthPermissionUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(AuthPermissionUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(AuthPermissionUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(AuthPermissionUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(AuthPermissionUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(AuthPermissionUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(AuthPermissionUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(AuthPermissionUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AuthPermissionUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AuthPermissionUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthPermissionUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:auth_permission_detail", args=(self.object.pk,))


class AuthPermissionDeleteView(DeleteView):
    model = AuthPermission
    template_name = "salika/auth_permission_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "auth_permission"

    def __init__(self, **kwargs):
        return super(AuthPermissionDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AuthPermissionDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(AuthPermissionDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(AuthPermissionDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AuthPermissionDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(AuthPermissionDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(AuthPermissionDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(AuthPermissionDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AuthPermissionDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AuthPermissionDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthPermissionDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:auth_permission_list")
