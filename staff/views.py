from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from cart.models import Order, Product
from .mixins import StaffUserMixin


class StaffView(LoginRequiredMixin, StaffUserMixin, generic.ListView):
    template_name = 'staff/staff.html'
    queryset = Order.objects.filter(ordered=True).order_by('-ordered_date')
    paginate_by = 20
    context_object_name = 'orders'


class ProductListView(LoginRequiredMixin, StaffUserMixin, generic.ListView):
    template_name = 'staff/product_list.html'
    queryset = Order.objects.all()
    paginate_by = 20
    context_object_name = 'orders'


class ProductDeleteView(LoginRequiredMixin, StaffUserMixin, generic.DeleteView):
    template_name = 'staff/product_delete.html'
    queryset = Order.objects.all()

    def get_success_url(self):
        return reverse("staff:product-list")
