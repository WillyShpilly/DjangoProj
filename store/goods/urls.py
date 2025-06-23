from django.urls import path
from .views import get_all_the_goods, get_the_good, get_category


urlpatterns = [
    path('', get_all_the_goods, name='main_page'),
    path('category/<slug:cat_slug>/', get_category, name='category'),
    path('firearm/<slug:a_good_slug>/', get_the_good, name='firearm'),
] 