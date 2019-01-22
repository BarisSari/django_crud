from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Inventory
from ..forms import InventoryForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class InventoryListView(ListView):
    model = Inventory
    template_name = "salika/inventory_list.html"
    paginate_by = 20
    context_object_name = "inventory_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(InventoryListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(InventoryListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(InventoryListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(InventoryListView, self).get_queryset()

    def get_allow_empty(self):
        return super(InventoryListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(InventoryListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(InventoryListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(InventoryListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(InventoryListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(InventoryListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(InventoryListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(InventoryListView, self).get_template_names()


class InventoryDetailView(DetailView):
    model = Inventory
    template_name = "salika/inventory_detail.html"
    context_object_name = "inventory"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(InventoryDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(InventoryDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(InventoryDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(InventoryDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(InventoryDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(InventoryDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(InventoryDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(InventoryDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(InventoryDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(InventoryDetailView, self).get_template_names()


class InventoryCreateView(CreateView):
    model = Inventory
    form_class = InventoryForm
    # fields = ['inventory_id', 'film', 'store_id', 'last_update']
    template_name = "salika/inventory_create.html"
    success_url = reverse_lazy("inventory_list")

    def __init__(self, **kwargs):
        return super(InventoryCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(InventoryCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(InventoryCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(InventoryCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(InventoryCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(InventoryCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(InventoryCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(InventoryCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(InventoryCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(InventoryCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(InventoryCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(InventoryCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(InventoryCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:inventory_detail", args=(self.object.pk,))


class InventoryUpdateView(UpdateView):
    model = Inventory
    form_class = InventoryForm
    # fields = ['inventory_id', 'film', 'store_id', 'last_update']
    template_name = "salika/inventory_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "inventory"

    def __init__(self, **kwargs):
        return super(InventoryUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(InventoryUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(InventoryUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(InventoryUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(InventoryUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(InventoryUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(InventoryUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(InventoryUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(InventoryUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(InventoryUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(InventoryUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(InventoryUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(InventoryUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(InventoryUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(InventoryUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(InventoryUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(InventoryUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:inventory_detail", args=(self.object.pk,))


class InventoryDeleteView(DeleteView):
    model = Inventory
    template_name = "salika/inventory_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "inventory"

    def __init__(self, **kwargs):
        return super(InventoryDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(InventoryDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(InventoryDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(InventoryDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(InventoryDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(InventoryDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(InventoryDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(InventoryDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(InventoryDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(InventoryDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(InventoryDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:inventory_list")
