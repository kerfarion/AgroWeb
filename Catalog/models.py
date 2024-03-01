from django.db import models
from django.urls import reverse


class Kind(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)

    class Meta:
        ordering = ("name", )

        verbose_name = "Вид товара"
        verbose_name_plural = "Виды товаров"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Catalog:product_list_by_category',
                       args=[self.slug])


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=150, db_index=True, unique=True)
    category = models.ForeignKey(Kind,
                                 on_delete=models.CASCADE,
                                 blank=True,
                                 null=True,
                                 )

    class Meta:
        ordering = ("name", )

        verbose_name = "Расшифровка"
        verbose_name_plural = "Расшифровки"

    def __str__(self):
        return self.name


class Product(models.Model):
    kind = models.ForeignKey(Kind,
                             related_name="kinds",
                             on_delete=models.CASCADE,
                             blank=True,
                             null=True
                             )

    category = models.ManyToManyField(Category,
                                      related_name="categories",
                                      blank=True,
                                      )

    name = models.CharField(max_length=75, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to="products/", blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=0)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("name",)

        index_together = (("id", "slug"), )
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:products_detail',
                       args=[self.id, self.slug])
