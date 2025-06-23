from django.shortcuts import render, get_object_or_404

from .models import Goods, Category
# Create your views here.


def get_all_the_goods(request):
    goods = Goods.available.all()

    data = {
        "title": "The main page",
        "goods": goods,
        "cat_selected": 0,
    }
    return render(request, "goods/index.html", context=data)


def get_category(request, cat_slug):
    category = get_object_or_404(Category, slug = cat_slug)
    goods = Goods.available.filter(category_id = category.pk)
    data = {
        "title": category.name,
        "goods": goods,
        "cat_selected": category.pk,
    }
    return render(request, "goods/index.html", context=data)


def get_the_good(request, a_good_slug):
    good = get_object_or_404(Goods, slug = a_good_slug)
    
    data = {
        "title": good.name,
        "good": good,
    }
    
    return render(request, "goods/firearm_detail.html", context=data) 