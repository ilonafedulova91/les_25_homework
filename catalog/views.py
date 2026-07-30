from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from .forms import ProductForm
from .models import Product

from django.contrib.auth.mixins import LoginRequiredMixin


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


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("home")

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("home")

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_delete.html"
    success_url = reverse_lazy("home")

# 3. Configure the URLs
