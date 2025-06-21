from django.urls import path
from .views import get_all_the_goods, get_category, get_the_good


urlpatterns = [
    path('', get_all_the_goods, name='main_page'),
    path('category/<slug:slug>/', get_category, name='category'),
    path('<slug:slug>/', get_the_good, name='firearm'),
]