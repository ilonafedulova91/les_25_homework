from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from .forms import ProductForm
from .models import Product


# Create your views here.
def home(request):
    products = Product.objects.all()

    paginator = Paginator(products, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
    }

    return render(request, "catalog/home.html", context)


def contacts(request):
    success = None
    name = None
    phone = None
    message = None

    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        print(name, phone, message)

        success = "Сообщение успешно отправлено!"

    return render(
        request,
        "catalog/contacts.html",
        {
            "success": success,
            "name": name,
            "phone": phone,
            "message": message,
        },
    )


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)

    context = {
        "product": product,
    }

    return render(request, "catalog/product_detail.html", context)


def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = ProductForm()

    return render(request, "catalog/product_form.html", {"form": form})


# 3. Configure the URLs
