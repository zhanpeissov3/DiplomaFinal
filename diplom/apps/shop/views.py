from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Service
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UserMessageForm, UserMessageServiceForm
from django.urls import reverse


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def get_services(request):
    list_services = Service.objects.all()
    return render(request, 'shop/services.html', {'list_services': list_services})


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request,
                  'shop/detail.html',
                  {'product': product})


def send_message(request):
    if request.method == 'POST':
        form = UserMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('shop:product_list'))
        else:
            return HttpResponse('<h1>Form nicht ausgefüllt</h1>')


def send_service(request):
    if request.method == 'POST':
        form = UserMessageServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('shop:get_services'))
        else:
            return HttpResponse('<h1>Form nicht ausgefüllt</h1>')
