from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import BlogFrom
from .models import Blog


class BlogListView(ListView):
    model = Blog
    context_object_name = "blog/blog_list.html"

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"

    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        object.views_count += 1
        object.save()
        return object


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogFrom
    template_name = "blog/blog_form.html"

    def get_success_url(self):
        return reverse("blog:detail", args=[self.object.pk])


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogFrom
    template_name = "blog/blog_form.html"
    success_url = reverse_lazy("blog:list")


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = "blog/blog_delete.html"
    success_url = reverse_lazy("blog:list")


# Create your views here.
