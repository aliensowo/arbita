from django.shortcuts import render
from django.views import View
from .models import Category_fb, Product_fb
from .models import Category_offer, Product_offer


def index_site(request, *args, **kwargs):
    template_name = 'index.html'

    return render(request, template_name=template_name)


def site1_1(request, category_slug=None):
    template_name = '1-1.html'
    category = None
    categories = Category_fb.objects.all()
    products = Product_fb.objects.filter()
    if category_slug:
        #category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, '1-1.html', {
        'category': category,
        'categories': categories,
        'products': products,
    })


def site1_6(request, category_slug=None):
    template_name = '1-6.html'
    category = None
    categories = Category_offer.objects.all()
    products = Product_offer.objects.filter()
    if category_slug:
        products = products.filter(category=category)
    return render(request, '1-6.html',{
        'category' : category,
        'categories' : categories,
        'products' : products
    })


def site1_7(request, *args, **kwargs):
    template_name = '1-7.html'

    return render(request, template_name=template_name)


def site1_8(request, *args, **kwargs):
    template_name = '1-8.html'

    return render(request, template_name=template_name)


def site1_9(request, *args, **kwargs):
    template_name = '1-9.html'

    return render(request, template_name=template_name)


def site1_10(request, *args, **kwargs):
    template_name = '1-10.html'

    return render(request, template_name=template_name)


def site1_11(request, *args, **kwargs):
    template_name = '1-11.html'

    return render(request, template_name=template_name)


def site1_12(request, *args, **kwargs):
    template_name = '1-12.html'

    return render(request, template_name=template_name)


def site1_13(request, *args, **kwargs):
    template_name = '1-13.html'

    return render(request, template_name=template_name)


def site1_15(request, *args, **kwargs):
    template_name = '1-15.html'

    return render(request, template_name=template_name)


def site1_16(request, *args, **kwargs):
    template_name = '1-16.html'

    return render(request, template_name=template_name)