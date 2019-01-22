from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Payment
from ..forms import PaymentForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class PaymentListView(ListView):
    model = Payment
    template_name = "salika/payment_list.html"
    paginate_by = 20
    context_object_name = "payment_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(PaymentListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PaymentListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PaymentListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(PaymentListView, self).get_queryset()

    def get_allow_empty(self):
        return super(PaymentListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(PaymentListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(PaymentListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(PaymentListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(PaymentListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(PaymentListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(PaymentListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PaymentListView, self).get_template_names()


class PaymentDetailView(DetailView):
    model = Payment
    template_name = "salika/payment_detail.html"
    context_object_name = "payment"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(PaymentDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PaymentDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PaymentDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PaymentDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(PaymentDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(PaymentDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(PaymentDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PaymentDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PaymentDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PaymentDetailView, self).get_template_names()


class PaymentCreateView(CreateView):
    model = Payment
    form_class = PaymentForm
    # fields = ['payment_id', 'customer', 'staff', 'rental', 'amount', 'payment_date']
    template_name = "salika/payment_create.html"
    success_url = reverse_lazy("payment_list")

    def __init__(self, **kwargs):
        return super(PaymentCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(PaymentCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PaymentCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(PaymentCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(PaymentCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(PaymentCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(PaymentCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(PaymentCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(PaymentCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(PaymentCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(PaymentCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(PaymentCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PaymentCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:payment_detail", args=(self.object.pk,))


class PaymentUpdateView(UpdateView):
    model = Payment
    form_class = PaymentForm
    # fields = ['payment_id', 'customer', 'staff', 'rental', 'amount', 'payment_date']
    template_name = "salika/payment_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "payment"

    def __init__(self, **kwargs):
        return super(PaymentUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PaymentUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PaymentUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(PaymentUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PaymentUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(PaymentUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(PaymentUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(PaymentUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(PaymentUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(PaymentUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(PaymentUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(PaymentUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(PaymentUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(PaymentUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PaymentUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PaymentUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PaymentUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:payment_detail", args=(self.object.pk,))


class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = "salika/payment_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "payment"

    def __init__(self, **kwargs):
        return super(PaymentDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PaymentDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(PaymentDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(PaymentDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PaymentDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(PaymentDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(PaymentDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(PaymentDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PaymentDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PaymentDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PaymentDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("salika:payment_list")
