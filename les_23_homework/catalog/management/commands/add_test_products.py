from django.core.management.base import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):
    help = 'Удаляет старые товары и добавляет тестовые продукты'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write(
            self.style.WARNING('Удалены старые данные')
        )

        electronics = Category.objects.create(
            name = 'Электроника',
            description = 'Электронные устройства',
        )

        books = Category.objects.create(
            name="Книги",
            description="Печатные и цифровые книги"
        )

        clothes = Category.objects.create(
            name="Одежда",
            description="Различные виды одежды"
        )

        Product.objects.create(
            name = 'Ноутбук',
            description = 'Мощный ноутбук для работы и учёбы',
            purchase_price = 1200,
            category = electronics,
        )

        Product.objects.create(
            name="Смартфон",
            description="Современный смартфон",
            purchase_price=800,
            category=electronics
        )

        Product.objects.create(
            name="Python Книга",
            description="Книга о Python программировании",
            purchase_price=50,
            category=books
        )

        Product.objects.create(
            name="Футболка",
            description="Футболка хлопковая",
            purchase_price=20,
            category=clothes
        )

        self.stdout.write(
            self.style.SUCCESS('Новые продукты успешно добавлены')
        )
