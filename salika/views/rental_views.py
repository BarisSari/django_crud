from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Rental
from ..forms import RentalForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class RentalListView(ListView):
    model = Rental
    template_name = "salika/rental_list.html"
    paginate_by = 20
    context_object_name = "rental_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(RentalListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RentalListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RentalListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(RentalListView, self).get_queryset()

    def get_allow_empty(self):
        return super(RentalListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(RentalListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(RentalListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(RentalListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(RentalListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(RentalListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(RentalListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RentalListView, self).get_template_names()


class RentalDetailView(DetailView):
    model = Rental
    template_name = "salika/rental_detail.html"
    context_object_name = "rental"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(RentalDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RentalDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RentalDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(RentalDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(RentalDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(RentalDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(RentalDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(RentalDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(RentalDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RentalDetailView, self).get_template_names()


class RentalCreateView(CreateView):
    model = Rental
    form_class = RentalForm
    # fields = ['rental_id', 'rental_date', 'inventory', 'customer', 'return_date', 'staff', 'last_update']
    template_name = "salika/rental_create.html"
    success_url = reverse_lazy("rental_list")

    def __init__(self, **kwargs):
        return super(RentalCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(RentalCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RentalCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(RentalCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(RentalCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(RentalCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(RentalCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(RentalCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(RentalCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(RentalCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(RentalCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(RentalCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RentalCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:rental_detail", args=(self.object.pk,))


class RentalUpdateView(UpdateView):
    model = Rental
    form_class = RentalForm
    # fields = ['rental_id', 'rental_date', 'inventory', 'customer', 'return_date', 'staff', 'last_update']
    template_name = "salika/rental_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "rental"

    def __init__(self, **kwargs):
        return super(RentalUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RentalUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(RentalUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(RentalUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(RentalUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(RentalUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(RentalUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(RentalUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(RentalUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(RentalUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(RentalUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(RentalUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(RentalUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(RentalUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(RentalUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(RentalUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RentalUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:rental_detail", args=(self.object.pk,))


class RentalDeleteView(DeleteView):
    model = Rental
    template_name = "salika/rental_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "rental"

    def __init__(self, **kwargs):
        return super(RentalDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(RentalDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(RentalDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(RentalDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(RentalDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(RentalDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(RentalDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(RentalDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(RentalDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(RentalDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(RentalDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:rental_list")
