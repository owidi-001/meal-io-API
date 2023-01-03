# Generated by Django 4.1.3 on 2022-12-22 20:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("vendor", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("icon", models.ImageField(upload_to="category//%Y/%m/%d/")),
                (
                    "date_created",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
            ],
            options={
                "verbose_name": "categories",
                "verbose_name_plural": "categories",
                "ordering": ("name", "-date_created"),
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                (
                    "unit",
                    models.CharField(
                        choices=[
                            ("kg", "kg"),
                            ("g", "g"),
                            ("l", "l"),
                            ("ml", "ml"),
                            ("in", "in"),
                        ],
                        default="kg",
                        help_text="Quantity measurement metrics",
                        max_length=2,
                    ),
                ),
                (
                    "unit_price",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Price per given unit",
                        max_digits=5,
                        verbose_name="unit price",
                    ),
                ),
                ("image", models.ImageField(upload_to="product//%Y/%m/%d/")),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="description"),
                ),
                ("stock", models.PositiveIntegerField(default=1, verbose_name="stock")),
                ("date_added", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.category",
                    ),
                ),
                (
                    "vendor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="vendor.vendor"
                    ),
                ),
            ],
            options={
                "verbose_name": "product",
                "verbose_name_plural": "products",
                "ordering": ("name", "-date_added"),
            },
        ),
    ]