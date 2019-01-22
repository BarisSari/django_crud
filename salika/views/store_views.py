from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Store
from ..forms import StoreForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class StoreListView(ListView):
    model = Store
    template_name = "salika/store_list.html"
    paginate_by = 20
    context_object_name = "store_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(StoreListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(StoreListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(StoreListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(StoreListView, self).get_queryset()

    def get_allow_empty(self):
        return super(StoreListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(StoreListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(StoreListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(StoreListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(StoreListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(StoreListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(StoreListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(StoreListView, self).get_template_names()


class StoreDetailView(DetailView):
    model = Store
    template_name = "salika/store_detail.html"
    context_object_name = "store"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(StoreDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(StoreDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(StoreDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(StoreDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(StoreDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(StoreDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(StoreDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(StoreDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(StoreDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(StoreDetailView, self).get_template_names()


class StoreCreateView(CreateView):
    model = Store
    form_class = StoreForm
    # fields = ['store_id', 'manager_staff', 'address', 'last_update']
    template_name = "salika/store_create.html"
    success_url = reverse_lazy("store_list")

    def __init__(self, **kwargs):
        return super(StoreCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(StoreCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(StoreCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(StoreCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(StoreCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(StoreCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(StoreCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(StoreCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(StoreCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(StoreCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(StoreCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(StoreCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(StoreCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:store_detail", args=(self.object.pk,))


class StoreUpdateView(UpdateView):
    model = Store
    form_class = StoreForm
    # fields = ['store_id', 'manager_staff', 'address', 'last_update']
    template_name = "salika/store_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "store"

    def __init__(self, **kwargs):
        return super(StoreUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(StoreUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(StoreUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(StoreUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(StoreUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(StoreUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(StoreUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(StoreUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(StoreUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(StoreUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(StoreUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(StoreUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(StoreUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(StoreUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(StoreUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(StoreUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(StoreUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:store_detail", args=(self.object.pk,))


class StoreDeleteView(DeleteView):
    model = Store
    template_name = "salika/store_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "store"

    def __init__(self, **kwargs):
        return super(StoreDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(StoreDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(StoreDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(StoreDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(StoreDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(StoreDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(StoreDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(StoreDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(StoreDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(StoreDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(StoreDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:store_list")
