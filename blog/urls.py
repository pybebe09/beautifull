from tkinter.font import names

from django.urls import path
from .views import index, contact,products,client,about, detail
urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('products/', products, name='products'),
    path('client/', client, name='client'),
    path('about/', about, name='about'),
    path('detail/<int:id>',detail, name='detail' )
]