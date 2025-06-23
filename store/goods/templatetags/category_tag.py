from django import template
import goods.views as views
from goods.models import Category

register = template.Library()



@register.inclusion_tag("goods/category.html")
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {"cats": cats, "cat_selected": cat_selected}