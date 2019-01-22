from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import DjangoContentType
from ..forms import DjangoContentTypeForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class DjangoContentTypeListView(ListView):
    model = DjangoContentType
    template_name = "salika/django_content_type_list.html"
    paginate_by = 20
    context_object_name = "django_content_type_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(DjangoContentTypeListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DjangoContentTypeListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DjangoContentTypeListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(DjangoContentTypeListView, self).get_queryset()

    def get_allow_empty(self):
        return super(DjangoContentTypeListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(DjangoContentTypeListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(DjangoContentTypeListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(DjangoContentTypeListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(DjangoContentTypeListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(DjangoContentTypeListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(DjangoContentTypeListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DjangoContentTypeListView, self).get_template_names()


class DjangoContentTypeDetailView(DetailView):
    model = DjangoContentType
    template_name = "salika/django_content_type_detail.html"
    context_object_name = "django_content_type"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(DjangoContentTypeDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DjangoContentTypeDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DjangoContentTypeDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DjangoContentTypeDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(DjangoContentTypeDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(DjangoContentTypeDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(DjangoContentTypeDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DjangoContentTypeDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DjangoContentTypeDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DjangoContentTypeDetailView, self).get_template_names()


class DjangoContentTypeCreateView(CreateView):
    model = DjangoContentType
    form_class = DjangoContentTypeForm
    # fields = ['app_label', 'model']
    template_name = "salika/django_content_type_create.html"
    success_url = reverse_lazy("django_content_type_list")

    def __init__(self, **kwargs):
        return super(DjangoContentTypeCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(DjangoContentTypeCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DjangoContentTypeCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(DjangoContentTypeCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(DjangoContentTypeCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(DjangoContentTypeCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(DjangoContentTypeCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(DjangoContentTypeCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(DjangoContentTypeCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(DjangoContentTypeCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(DjangoContentTypeCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(DjangoContentTypeCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DjangoContentTypeCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:django_content_type_detail", args=(self.object.pk,))


class DjangoContentTypeUpdateView(UpdateView):
    model = DjangoContentType
    form_class = DjangoContentTypeForm
    # fields = ['app_label', 'model']
    template_name = "salika/django_content_type_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "django_content_type"

    def __init__(self, **kwargs):
        return super(DjangoContentTypeUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DjangoContentTypeUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DjangoContentTypeUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(DjangoContentTypeUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DjangoContentTypeUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(DjangoContentTypeUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(DjangoContentTypeUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(DjangoContentTypeUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(DjangoContentTypeUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(DjangoContentTypeUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(DjangoContentTypeUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(DjangoContentTypeUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(DjangoContentTypeUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(DjangoContentTypeUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DjangoContentTypeUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DjangoContentTypeUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DjangoContentTypeUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:django_content_type_detail", args=(self.object.pk,))


class DjangoContentTypeDeleteView(DeleteView):
    model = DjangoContentType
    template_name = "salika/django_content_type_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "django_content_type"

    def __init__(self, **kwargs):
        return super(DjangoContentTypeDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DjangoContentTypeDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(DjangoContentTypeDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(DjangoContentTypeDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DjangoContentTypeDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(DjangoContentTypeDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(DjangoContentTypeDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(DjangoContentTypeDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DjangoContentTypeDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DjangoContentTypeDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DjangoContentTypeDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:django_content_type_list")
