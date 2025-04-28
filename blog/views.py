from django.shortcuts import render
from .models import Product,About
# Create your views here.
def index(request):
    products = Product.objects.all()
    carousel = products.filter(joylash = 'caro')
    product = products.filter(joylash = 'pro')
    about = About.objects.all()
    malumot = {
        "caro": carousel,
        "pro": product,
        "about": about,
    }
    return render(request, 'pages/index.html', context = malumot)

def about(request):
    about=About.objects.all()
    s={
        "about":about,
    }
    return render(request, 'pages/about.html', context =s)

def client(request):
    return render(request, 'pages/client.html', context = {})

def products(request):
    return render(request, 'pages/products.html', context = {})

def contact(request):
    return render(request, 'pages/contact.html', context = {})

def detail(request, id):
    product = Product.objects.get(id=id)
    context = {
        'x': product
    }
    return render(request, 'detail/detail.html', context = context)