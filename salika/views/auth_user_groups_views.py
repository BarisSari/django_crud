from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import AuthUserGroups
from ..forms import AuthUserGroupsForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class AuthUserGroupsListView(ListView):
    model = AuthUserGroups
    template_name = "salika/auth_user_groups_list.html"
    paginate_by = 20
    context_object_name = "auth_user_groups_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(AuthUserGroupsListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AuthUserGroupsListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AuthUserGroupsListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(AuthUserGroupsListView, self).get_queryset()

    def get_allow_empty(self):
        return super(AuthUserGroupsListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(AuthUserGroupsListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(AuthUserGroupsListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(AuthUserGroupsListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(AuthUserGroupsListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(AuthUserGroupsListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(AuthUserGroupsListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthUserGroupsListView, self).get_template_names()


class AuthUserGroupsDetailView(DetailView):
    model = AuthUserGroups
    template_name = "salika/auth_user_groups_detail.html"
    context_object_name = "auth_user_groups"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(AuthUserGroupsDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AuthUserGroupsDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AuthUserGroupsDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AuthUserGroupsDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(AuthUserGroupsDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(AuthUserGroupsDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(AuthUserGroupsDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AuthUserGroupsDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AuthUserGroupsDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthUserGroupsDetailView, self).get_template_names()


class AuthUserGroupsCreateView(CreateView):
    model = AuthUserGroups
    form_class = AuthUserGroupsForm
    # fields = ['user', 'group']
    template_name = "salika/auth_user_groups_create.html"
    success_url = reverse_lazy("auth_user_groups_list")

    def __init__(self, **kwargs):
        return super(AuthUserGroupsCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(AuthUserGroupsCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AuthUserGroupsCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(AuthUserGroupsCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(AuthUserGroupsCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(AuthUserGroupsCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(AuthUserGroupsCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(AuthUserGroupsCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(AuthUserGroupsCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(AuthUserGroupsCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(AuthUserGroupsCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(AuthUserGroupsCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthUserGroupsCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:auth_user_groups_detail", args=(self.object.pk,))


class AuthUserGroupsUpdateView(UpdateView):
    model = AuthUserGroups
    form_class = AuthUserGroupsForm
    # fields = ['user', 'group']
    template_name = "salika/auth_user_groups_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "auth_user_groups"

    def __init__(self, **kwargs):
        return super(AuthUserGroupsUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AuthUserGroupsUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AuthUserGroupsUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(AuthUserGroupsUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AuthUserGroupsUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(AuthUserGroupsUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(AuthUserGroupsUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(AuthUserGroupsUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(AuthUserGroupsUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(AuthUserGroupsUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(AuthUserGroupsUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(AuthUserGroupsUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(AuthUserGroupsUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(AuthUserGroupsUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AuthUserGroupsUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AuthUserGroupsUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthUserGroupsUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:auth_user_groups_detail", args=(self.object.pk,))


class AuthUserGroupsDeleteView(DeleteView):
    model = AuthUserGroups
    template_name = "salika/auth_user_groups_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "auth_user_groups"

    def __init__(self, **kwargs):
        return super(AuthUserGroupsDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AuthUserGroupsDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(AuthUserGroupsDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(AuthUserGroupsDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AuthUserGroupsDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(AuthUserGroupsDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(AuthUserGroupsDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(AuthUserGroupsDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AuthUserGroupsDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AuthUserGroupsDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthUserGroupsDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:auth_user_groups_list")
