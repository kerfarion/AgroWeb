# Generated by Django 5.0.1 on 2024-02-09 18:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0004_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Catalog.kind'),
        ),
    ]
