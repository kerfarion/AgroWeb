# Generated by Django 5.0.1 on 2024-02-11 09:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0005_category_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, limit_choices_to={'Category': models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kinds', to='Catalog.kind')}, related_name='categories', to='Catalog.category'),
        ),
    ]
