from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Address
from ..forms import AddressForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class AddressListView(ListView):
    model = Address
    template_name = "salika/address_list.html"
    paginate_by = 20
    context_object_name = "address_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(AddressListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AddressListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AddressListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(AddressListView, self).get_queryset()

    def get_allow_empty(self):
        return super(AddressListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(AddressListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(AddressListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(AddressListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(AddressListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(AddressListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(AddressListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AddressListView, self).get_template_names()


class AddressDetailView(DetailView):
    model = Address
    template_name = "salika/address_detail.html"
    context_object_name = "address"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(AddressDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AddressDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AddressDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AddressDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(AddressDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(AddressDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(AddressDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AddressDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AddressDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AddressDetailView, self).get_template_names()


class AddressCreateView(CreateView):
    model = Address
    form_class = AddressForm
    # fields = ['address_id', 'address', 'address2', 'district', 'city', 'postal_code', 'phone', 'last_update']
    template_name = "salika/address_create.html"
    success_url = reverse_lazy("address_list")

    def __init__(self, **kwargs):
        return super(AddressCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(AddressCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AddressCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(AddressCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(AddressCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(AddressCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(AddressCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(AddressCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(AddressCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(AddressCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(AddressCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(AddressCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AddressCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:address_detail", args=(self.object.pk,))


class AddressUpdateView(UpdateView):
    model = Address
    form_class = AddressForm
    # fields = ['address_id', 'address', 'address2', 'district', 'city', 'postal_code', 'phone', 'last_update']
    template_name = "salika/address_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "address"

    def __init__(self, **kwargs):
        return super(AddressUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AddressUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(AddressUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(AddressUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AddressUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(AddressUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(AddressUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(AddressUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(AddressUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(AddressUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(AddressUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(AddressUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(AddressUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(AddressUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AddressUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AddressUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AddressUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:address_detail", args=(self.object.pk,))


class AddressDeleteView(DeleteView):
    model = Address
    template_name = "salika/address_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "address"

    def __init__(self, **kwargs):
        return super(AddressDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(AddressDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(AddressDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(AddressDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(AddressDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(AddressDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(AddressDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(AddressDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(AddressDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(AddressDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(AddressDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:address_list")
