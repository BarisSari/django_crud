from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import AuthUserUserPermissions
from ..forms import AuthUserUserPermissionsForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class AuthUserUserPermissionsListView(ListView):
    model = AuthUserUserPermissions
    template_name = "salika/auth_user_user_permissions_list.html"
    paginate_by = 20
    context_object_name = "auth_user_user_permissions_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(AuthUserUserPermissionsListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AuthUserUserPermissionsListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AuthUserUserPermissionsListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(AuthUserUserPermissionsListView, self).get_queryset()

    def get_allow_empty(self):
        return super(AuthUserUserPermissionsListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(AuthUserUserPermissionsListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(AuthUserUserPermissionsListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(AuthUserUserPermissionsListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(AuthUserUserPermissionsListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(AuthUserUserPermissionsListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(AuthUserUserPermissionsListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthUserUserPermissionsListView, self).get_template_names()


class AuthUserUserPermissionsDetailView(DetailView):
    model = AuthUserUserPermissions
    template_name = "salika/auth_user_user_permissions_detail.html"
    context_object_name = "auth_user_user_permissions"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(AuthUserUserPermissionsDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AuthUserUserPermissionsDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AuthUserUserPermissionsDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AuthUserUserPermissionsDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(AuthUserUserPermissionsDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(AuthUserUserPermissionsDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(AuthUserUserPermissionsDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AuthUserUserPermissionsDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AuthUserUserPermissionsDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthUserUserPermissionsDetailView, self).get_template_names()


class AuthUserUserPermissionsCreateView(CreateView):
    model = AuthUserUserPermissions
    form_class = AuthUserUserPermissionsForm
    # fields = ['user', 'permission']
    template_name = "salika/auth_user_user_permissions_create.html"
    success_url = reverse_lazy("auth_user_user_permissions_list")

    def __init__(self, **kwargs):
        return super(AuthUserUserPermissionsCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(AuthUserUserPermissionsCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AuthUserUserPermissionsCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(AuthUserUserPermissionsCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(AuthUserUserPermissionsCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(AuthUserUserPermissionsCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(AuthUserUserPermissionsCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(AuthUserUserPermissionsCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(AuthUserUserPermissionsCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(AuthUserUserPermissionsCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(AuthUserUserPermissionsCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(AuthUserUserPermissionsCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthUserUserPermissionsCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:auth_user_user_permissions_detail", args=(self.object.pk,))


class AuthUserUserPermissionsUpdateView(UpdateView):
    model = AuthUserUserPermissions
    form_class = AuthUserUserPermissionsForm
    # fields = ['user', 'permission']
    template_name = "salika/auth_user_user_permissions_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "auth_user_user_permissions"

    def __init__(self, **kwargs):
        return super(AuthUserUserPermissionsUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AuthUserUserPermissionsUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AuthUserUserPermissionsUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(AuthUserUserPermissionsUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AuthUserUserPermissionsUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(AuthUserUserPermissionsUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(AuthUserUserPermissionsUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(AuthUserUserPermissionsUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(AuthUserUserPermissionsUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(AuthUserUserPermissionsUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(AuthUserUserPermissionsUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(AuthUserUserPermissionsUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(AuthUserUserPermissionsUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(AuthUserUserPermissionsUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AuthUserUserPermissionsUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AuthUserUserPermissionsUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthUserUserPermissionsUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:auth_user_user_permissions_detail", args=(self.object.pk,))


class AuthUserUserPermissionsDeleteView(DeleteView):
    model = AuthUserUserPermissions
    template_name = "salika/auth_user_user_permissions_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "auth_user_user_permissions"

    def __init__(self, **kwargs):
        return super(AuthUserUserPermissionsDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AuthUserUserPermissionsDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(AuthUserUserPermissionsDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(AuthUserUserPermissionsDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AuthUserUserPermissionsDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(AuthUserUserPermissionsDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(AuthUserUserPermissionsDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(AuthUserUserPermissionsDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AuthUserUserPermissionsDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AuthUserUserPermissionsDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthUserUserPermissionsDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:auth_user_user_permissions_list")
