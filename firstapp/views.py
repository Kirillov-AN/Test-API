from django.views.generic import View
from .api import CategoryMixin
from .models import Category


class Classcat(CategoryMixin, View):
    model = Category
    
