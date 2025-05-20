from django.urls import path
from django.contrib.auth.views import LogoutView,LoginView,PasswordChangeView,PasswordChangeDoneView
from .views import logout_view, sign_up, profile_view, profile_edit
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetCompleteView,PasswordResetConfirmView
urlpatterns=[
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('logout_view/',logout_view,name='logout_view'),
    path('sign_up',sign_up,name='sign_up'),
    path('profile/',profile_view,name='profile'),
    path('profile_edit',profile_edit,name='profile_edit'),

    path('password_change/',PasswordChangeView.as_view(),name='password_change'),
    path('password_change/done/',PasswordChangeDoneView.as_view(),name='password_change_done'),

    path('password_reset/',PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',PasswordResetCompleteView.as_view(),name='password_reset_complete')


]