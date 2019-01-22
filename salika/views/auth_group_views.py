from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import AuthGroup
from ..forms import AuthGroupForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class AuthGroupListView(ListView):
    model = AuthGroup
    template_name = "salika/auth_group_list.html"
    paginate_by = 20
    context_object_name = "auth_group_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(AuthGroupListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AuthGroupListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AuthGroupListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(AuthGroupListView, self).get_queryset()

    def get_allow_empty(self):
        return super(AuthGroupListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(AuthGroupListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(AuthGroupListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(AuthGroupListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(AuthGroupListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(AuthGroupListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(AuthGroupListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthGroupListView, self).get_template_names()


class AuthGroupDetailView(DetailView):
    model = AuthGroup
    template_name = "salika/auth_group_detail.html"
    context_object_name = "auth_group"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(AuthGroupDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AuthGroupDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AuthGroupDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AuthGroupDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(AuthGroupDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(AuthGroupDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(AuthGroupDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AuthGroupDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AuthGroupDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthGroupDetailView, self).get_template_names()


class AuthGroupCreateView(CreateView):
    model = AuthGroup
    form_class = AuthGroupForm
    # fields = ['name']
    template_name = "salika/auth_group_create.html"
    success_url = reverse_lazy("auth_group_list")

    def __init__(self, **kwargs):
        return super(AuthGroupCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(AuthGroupCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AuthGroupCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(AuthGroupCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(AuthGroupCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(AuthGroupCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(AuthGroupCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(AuthGroupCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(AuthGroupCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(AuthGroupCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(AuthGroupCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(AuthGroupCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthGroupCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:auth_group_detail", args=(self.object.pk,))


class AuthGroupUpdateView(UpdateView):
    model = AuthGroup
    form_class = AuthGroupForm
    # fields = ['name']
    template_name = "salika/auth_group_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "auth_group"

    def __init__(self, **kwargs):
        return super(AuthGroupUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AuthGroupUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AuthGroupUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(AuthGroupUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AuthGroupUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(AuthGroupUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(AuthGroupUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(AuthGroupUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(AuthGroupUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(AuthGroupUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(AuthGroupUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(AuthGroupUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(AuthGroupUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(AuthGroupUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AuthGroupUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AuthGroupUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthGroupUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:auth_group_detail", args=(self.object.pk,))


class AuthGroupDeleteView(DeleteView):
    model = AuthGroup
    template_name = "salika/auth_group_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "auth_group"

    def __init__(self, **kwargs):
        return super(AuthGroupDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AuthGroupDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(AuthGroupDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(AuthGroupDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AuthGroupDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(AuthGroupDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(AuthGroupDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(AuthGroupDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AuthGroupDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AuthGroupDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AuthGroupDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:auth_group_list")
