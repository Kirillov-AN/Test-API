from django.urls import path
from .views import Classcat


urlpatterns = [
    path('categories/', Classcat.as_view()),
    path('categories/<str:id>', Classcat.as_view()),
]
