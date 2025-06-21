from django.shortcuts import render

# Create your views here.

def get_all_the_goods(request):
    return render(request, "goods/index.html")


def get_category(request, slug):
    data = {"text": slug}
    return render(request, "goods/category.html", data)


def get_the_good(request, slug):
    data = {"text": slug}
    return render(request, "goods/firearm_detail.html", data) 