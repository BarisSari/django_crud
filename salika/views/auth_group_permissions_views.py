from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import AuthGroupPermissions
from ..forms import AuthGroupPermissionsForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class AuthGroupPermissionsListView(ListView):
    model = AuthGroupPermissions
    template_name = "salika/auth_group_permissions_list.html"
    paginate_by = 20
    context_object_name = "auth_group_permissions_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(AuthGroupPermissionsListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AuthGroupPermissionsListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AuthGroupPermissionsListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(AuthGroupPermissionsListView, self).get_queryset()

    def get_allow_empty(self):
        return super(AuthGroupPermissionsListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(AuthGroupPermissionsListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(AuthGroupPermissionsListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(AuthGroupPermissionsListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(AuthGroupPermissionsListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(AuthGroupPermissionsListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(AuthGroupPermissionsListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthGroupPermissionsListView, self).get_template_names()


class AuthGroupPermissionsDetailView(DetailView):
    model = AuthGroupPermissions
    template_name = "salika/auth_group_permissions_detail.html"
    context_object_name = "auth_group_permissions"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(AuthGroupPermissionsDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AuthGroupPermissionsDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AuthGroupPermissionsDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AuthGroupPermissionsDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(AuthGroupPermissionsDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(AuthGroupPermissionsDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(AuthGroupPermissionsDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AuthGroupPermissionsDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AuthGroupPermissionsDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthGroupPermissionsDetailView, self).get_template_names()


class AuthGroupPermissionsCreateView(CreateView):
    model = AuthGroupPermissions
    form_class = AuthGroupPermissionsForm
    # fields = ['group', 'permission']
    template_name = "salika/auth_group_permissions_create.html"
    success_url = reverse_lazy("auth_group_permissions_list")

    def __init__(self, **kwargs):
        return super(AuthGroupPermissionsCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(AuthGroupPermissionsCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AuthGroupPermissionsCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(AuthGroupPermissionsCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(AuthGroupPermissionsCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(AuthGroupPermissionsCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(AuthGroupPermissionsCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(AuthGroupPermissionsCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(AuthGroupPermissionsCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(AuthGroupPermissionsCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(AuthGroupPermissionsCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(AuthGroupPermissionsCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthGroupPermissionsCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:auth_group_permissions_detail", args=(self.object.pk,))


class AuthGroupPermissionsUpdateView(UpdateView):
    model = AuthGroupPermissions
    form_class = AuthGroupPermissionsForm
    # fields = ['group', 'permission']
    template_name = "salika/auth_group_permissions_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "auth_group_permissions"

    def __init__(self, **kwargs):
        return super(AuthGroupPermissionsUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AuthGroupPermissionsUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AuthGroupPermissionsUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(AuthGroupPermissionsUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AuthGroupPermissionsUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(AuthGroupPermissionsUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(AuthGroupPermissionsUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(AuthGroupPermissionsUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(AuthGroupPermissionsUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(AuthGroupPermissionsUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(AuthGroupPermissionsUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(AuthGroupPermissionsUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(AuthGroupPermissionsUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(AuthGroupPermissionsUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AuthGroupPermissionsUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AuthGroupPermissionsUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthGroupPermissionsUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:auth_group_permissions_detail", args=(self.object.pk,))


class AuthGroupPermissionsDeleteView(DeleteView):
    model = AuthGroupPermissions
    template_name = "salika/auth_group_permissions_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "auth_group_permissions"

    def __init__(self, **kwargs):
        return super(AuthGroupPermissionsDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AuthGroupPermissionsDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(AuthGroupPermissionsDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(AuthGroupPermissionsDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AuthGroupPermissionsDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(AuthGroupPermissionsDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(AuthGroupPermissionsDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(AuthGroupPermissionsDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AuthGroupPermissionsDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AuthGroupPermissionsDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthGroupPermissionsDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:auth_group_permissions_list")
