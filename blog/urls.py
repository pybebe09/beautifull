from tkinter.font import names

from accaunts.views import profile_view
from .views import ProductCreate, ProductUpdate, ProductDelete
from django.urls import path
from django.contrib.auth.views import LogoutView,LoginView
from .views import index, contact,products,client,about, detail
urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('products/', products, name='products'),
    path('client/', client, name='client'),
    path('about/', about, name='about'),
    path('detail/<str:slug>',detail, name='detail' ),
    path('update/<int:pk>/', ProductUpdate.as_view(), name='update'),
    path('create/', ProductCreate.as_view(), name='create'),
    path('delete/<int:pk>',ProductDelete.as_view(),name='delete'),
    path('profile',profile_view,name='profile'),
    path('logout/', LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    path('login/', LoginView.as_view(), name='login'),

]