from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    parent = models.ForeignKey('self', blank=True, null=True,
                               related_name='children',on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
