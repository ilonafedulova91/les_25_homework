from django.forms import ModelForm

from .models import Blog


class BlogFrom(ModelForm):

    class Meta:
        model = Blog
        fields = "__all__"
