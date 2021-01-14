from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mainapp:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True, default='some_book')
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    diagonal = models.CharField(max_length=255, verbose_name='Diagonal', default='')
    display_type = models.CharField(max_length=255, verbose_name='Display type', default='')
    resolution = models.CharField(max_length=255, verbose_name='resolution', default='')
    accum_volume = models.CharField(max_length=255, verbose_name='Battery', default='')
    ram = models.CharField(max_length=255, verbose_name='RAM', default='')
    main_cam = models.CharField(max_length=255, verbose_name='Main camera', default='')
    frontal_cam = models.CharField(max_length=255, verbose_name='Selfie camera', default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mainapp:product_detail', args=[self.id, self.slug])

    def get_model_name(self):
        return self.__class__.__name__.lower()



class Comment(models.Model):
    post = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.text