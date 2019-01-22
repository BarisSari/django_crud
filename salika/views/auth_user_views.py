from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import AuthUser
from ..forms import AuthUserForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class AuthUserListView(ListView):
    model = AuthUser
    template_name = "salika/auth_user_list.html"
    paginate_by = 20
    context_object_name = "auth_user_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(AuthUserListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AuthUserListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AuthUserListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(AuthUserListView, self).get_queryset()

    def get_allow_empty(self):
        return super(AuthUserListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(AuthUserListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(AuthUserListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(AuthUserListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(AuthUserListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(AuthUserListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(AuthUserListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthUserListView, self).get_template_names()


class AuthUserDetailView(DetailView):
    model = AuthUser
    template_name = "salika/auth_user_detail.html"
    context_object_name = "auth_user"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(AuthUserDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AuthUserDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AuthUserDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AuthUserDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(AuthUserDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(AuthUserDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(AuthUserDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AuthUserDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AuthUserDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthUserDetailView, self).get_template_names()


class AuthUserCreateView(CreateView):
    model = AuthUser
    form_class = AuthUserForm
    # fields = ['password', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined']
    template_name = "salika/auth_user_create.html"
    success_url = reverse_lazy("auth_user_list")

    def __init__(self, **kwargs):
        return super(AuthUserCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(AuthUserCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AuthUserCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(AuthUserCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(AuthUserCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(AuthUserCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(AuthUserCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(AuthUserCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(AuthUserCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(AuthUserCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(AuthUserCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(AuthUserCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthUserCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:auth_user_detail", args=(self.object.pk,))


class AuthUserUpdateView(UpdateView):
    model = AuthUser
    form_class = AuthUserForm
    # fields = ['password', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined']
    template_name = "salika/auth_user_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "auth_user"

    def __init__(self, **kwargs):
        return super(AuthUserUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AuthUserUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AuthUserUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(AuthUserUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AuthUserUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(AuthUserUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(AuthUserUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(AuthUserUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(AuthUserUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(AuthUserUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(AuthUserUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(AuthUserUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(AuthUserUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(AuthUserUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AuthUserUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AuthUserUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthUserUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:auth_user_detail", args=(self.object.pk,))


class AuthUserDeleteView(DeleteView):
    model = AuthUser
    template_name = "salika/auth_user_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "auth_user"

    def __init__(self, **kwargs):
        return super(AuthUserDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AuthUserDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(AuthUserDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(AuthUserDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AuthUserDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(AuthUserDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(AuthUserDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(AuthUserDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AuthUserDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AuthUserDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthUserDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:auth_user_list")
