from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import FilmCategory
from ..forms import FilmCategoryForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class FilmCategoryListView(ListView):
    model = FilmCategory
    template_name = "salika/film_category_list.html"
    paginate_by = 20
    context_object_name = "film_category_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(FilmCategoryListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(FilmCategoryListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(FilmCategoryListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(FilmCategoryListView, self).get_queryset()

    def get_allow_empty(self):
        return super(FilmCategoryListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(FilmCategoryListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(FilmCategoryListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(FilmCategoryListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(FilmCategoryListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(FilmCategoryListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(FilmCategoryListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FilmCategoryListView, self).get_template_names()


class FilmCategoryDetailView(DetailView):
    model = FilmCategory
    template_name = "salika/film_category_detail.html"
    context_object_name = "film_category"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(FilmCategoryDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(FilmCategoryDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(FilmCategoryDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(FilmCategoryDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(FilmCategoryDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(FilmCategoryDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(FilmCategoryDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(FilmCategoryDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(FilmCategoryDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FilmCategoryDetailView, self).get_template_names()


class FilmCategoryCreateView(CreateView):
    model = FilmCategory
    form_class = FilmCategoryForm
    # fields = ['film', 'category', 'last_update']
    template_name = "salika/film_category_create.html"
    success_url = reverse_lazy("film_category_list")

    def __init__(self, **kwargs):
        return super(FilmCategoryCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(FilmCategoryCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(FilmCategoryCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(FilmCategoryCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(FilmCategoryCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(FilmCategoryCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(FilmCategoryCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(FilmCategoryCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(FilmCategoryCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(FilmCategoryCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(FilmCategoryCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(FilmCategoryCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FilmCategoryCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:film_category_detail", args=(self.object.pk,))


class FilmCategoryUpdateView(UpdateView):
    model = FilmCategory
    form_class = FilmCategoryForm
    # fields = ['film', 'category', 'last_update']
    template_name = "salika/film_category_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "film_category"

    def __init__(self, **kwargs):
        return super(FilmCategoryUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(FilmCategoryUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(FilmCategoryUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(FilmCategoryUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(FilmCategoryUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(FilmCategoryUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(FilmCategoryUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(FilmCategoryUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(FilmCategoryUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(FilmCategoryUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(FilmCategoryUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(FilmCategoryUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(FilmCategoryUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(FilmCategoryUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(FilmCategoryUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(FilmCategoryUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FilmCategoryUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:film_category_detail", args=(self.object.pk,))


class FilmCategoryDeleteView(DeleteView):
    model = FilmCategory
    template_name = "salika/film_category_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "film_category"

    def __init__(self, **kwargs):
        return super(FilmCategoryDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(FilmCategoryDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(FilmCategoryDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(FilmCategoryDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(FilmCategoryDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(FilmCategoryDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(FilmCategoryDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(FilmCategoryDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(FilmCategoryDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(FilmCategoryDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(FilmCategoryDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:film_category_list")
