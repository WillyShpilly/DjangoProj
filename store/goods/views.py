from django.shortcuts import render, get_object_or_404

from .models import Goods
# Create your views here.

def get_all_the_goods(request):
    goods = Goods.available.all()

    data = {
        "title": "The main page",
        "goods": goods
    }
    return render(request, "goods/index.html", context=data)


def get_category(request, cat_slug):
    # category = get_object_or_404(Category, slug = cat_slug)
    # data = {"text": cat_slug}
    return render(request, "goods/category.html")


def get_the_good(request, a_good_slug):
    good = get_object_or_404(Goods, a_good_slug)
    
    data = {
        "title": good.name,
        "good": good,
    }
    
    return render(request, "goods/firearm_detail.html", data) 