from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .forms import ProductForm
from .models import Product


# Create your views here.
class HomeListView(ListView):
    model = Product
    template_name = "catalog/home.html"
    paginate_by = 4


class ContactsView(View):
    template_name = "catalog/contacts.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        context = {
            "success": "Сообщение успешно отправлено!",
            "name": request.POST.get("name"),
            "phone": request.POST.get("phone"),
            "message": request.POST.get("message"),
        }

        print(
            context["name"],
            context["phone"],
            context["message"],
        )

        return render(request, self.template_name, context)


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()

        if product.owner != request.user:
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_delete.html"
    success_url = reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()

        if product.owner != request.user and not request.user.has_perm(
            "catalog.can_delete_product"
        ):
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)


class ProductUnpublishView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = "catalog.can_unpublish_product"

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.is_published = False
        product.save()

        return redirect("product_detail", pk=pk)


# 3. Configure the URLs
