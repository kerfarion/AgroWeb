# Generated by Django 5.0.1 on 2024-02-08 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='categories', to='Catalog.category'),
        ),
    ]
