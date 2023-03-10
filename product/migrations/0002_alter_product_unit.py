# Generated by Django 4.1.3 on 2023-01-05 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="unit",
            field=models.CharField(
                choices=[
                    ("kg", "kg"),
                    ("g", "g"),
                    ("l", "l"),
                    ("ml", "ml"),
                    ("in", "in"),
                    ("C", "Count"),
                ],
                default="kg",
                help_text="Quantity measurement metrics",
                max_length=2,
            ),
        ),
    ]
