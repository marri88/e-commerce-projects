from django.urls import path
from . import views
from shop import views as sviews
from django.contrib.auth import views


urlpatterns = [
    path('register/', views.LoginView, name='register'),
    path('edit/', views.LoginView, name='edit'),
    path('login/', views.LoginView, name='login'),
    path('logout/', sviews.logout_page, name='logout'),
    path('password_edit/', views.PasswordChangeView, name='password_edit'),
    path('user/(?P<username>[-\w]+)/', views.UserModel, name='user_detail'),
    path('password-change/', views.PasswordChangeView, name='password_change'),
    path('password-change/done/', views.PasswordChangeDoneView, name='password_change_done'),
    # restore password urls
    path('password-reset/', views.PasswordResetView, name='password_reset'),
    path('password-reset/done/', views.PasswordResetDoneView, name='password_reset_done'),
    path('password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/', views.PasswordResetConfirmView, name='password_reset_confirm'),
    path('password-reset/complete/', views.PasswordResetCompleteView, name='password_reset_complete'),
]

