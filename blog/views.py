from django.shortcuts import render, redirect
from django.views.generic import UpdateView, CreateView, DeleteView

from accaunts.forms import CommentForm
from accaunts.models import Comment
from .models import Product,About,Client
from django.urls import reverse_lazy
# Create your views here.
def index(request):
    products = Product.objects.all()
    carousel = products.filter(joylash = 'caro')
    product = products.filter(joylash = 'pro')
    about = About.objects.all()
    client = Client.objects.all()
    try:
        qidiruv=request.GET['text']
    except:
        qidiruv=False
    if qidiruv:
        product=products.filter(name__icontains=qidiruv)
    malumot = {
        "caro": carousel,
        "pro": product,
        "about": about,
        "client": client
    }
    return render(request, 'pages/index.html', context = malumot)

def about(request):
    about=About.objects.all()
    s={
        "about":about,
    }
    return render(request, 'pages/about.html', context =s)

def client(request):
    client=Client.objects.all()
    context={
        "client": client
    }
    return render(request, 'pages/client.html', context = context)

def products(request):
    products = Product.objects.all()
    carousel = products.filter(joylash = 'caro')
    product = products.filter(joylash = 'pro')
    context={
        "caro":carousel,
        "pro":product,
    }
    return render(request, 'pages/products.html', context =context)

def contact(request):
    return render(request, 'pages/contact.html', context = {})


def detail(request,slug):
    product = Product.objects.get(slug=slug)
    comments = Comment.objects.filter(product_id=product)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.product_id = product
            form.user = request.user
            form.save()
            return redirect('detail', slug)
    else:
        form = CommentForm()

    context = {
        "x": product,
        'comment': comments,
        'form': form
    }
    return render(request, 'detail/detail.html', context=context)

class ProductUpdate(UpdateView):
    model = Product
    template_name ='pages/update.html'
    fields = '__all__'
    success_url = reverse_lazy('index')
class ProductCreate(CreateView):
    model = Product
    template_name = 'pages/create.html'
    fields = '__all__'
    success_url = reverse_lazy('index')

class ProductDelete(DeleteView):
    model= Product
    template_name = 'pages/product_confirm_delete.html'
    success_url = reverse_lazy('index')

