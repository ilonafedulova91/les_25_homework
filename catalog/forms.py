from django import forms
from django.core.exceptions import ValidationError
from django.forms import CheckboxInput

from .models import Product

FORBIDDEN_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            "name",
            "description",
            "image",
            "category",
            "purchase_price",
            "is_published",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            if isinstance(field.widget, CheckboxInput):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"

        self.fields["name"].widget.attrs["placeholder"] = "Введите название товара"
        self.fields["description"].widget.attrs["placeholder"] = "Введите описание"
        self.fields["purchase_price"].widget.attrs["placeholder"] = "Введите цену"
        self.fields["is_published"].label = "Опубликовать товар"

    def clean_name(self):
        name = self.cleaned_data.get("name")

        if name:
            for word in FORBIDDEN_WORDS:
                if word.lower() in name.lower():
                    raise ValidationError("Название содержит запрещенное слово")

        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")

        if description:
            for word in FORBIDDEN_WORDS:
                if word.lower() in description.lower():
                    raise ValidationError("Описание содержит запрещенное слово")

        return description

    def clean_price(self):
        price = self.cleaned_data.get("purchase_price")

        if price < 0:
            raise ValidationError("Цена не может быть отрицательной")

        return price

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if image:
            allowed_formats = ["jpg", "jpeg", "png"]

            extension = image.name.rsplit(".", maxsplit=1)[-1]

            if extension not in allowed_formats:
                raise ValidationError(
                    "Допустимы только изображения формата JPEG или PNG"
                )

            if image.size > 5 * 1024 * 1024:
                raise ValidationError("Размер изображения не должен превышать 5 МБ")

        return image
