from django.urls import path
from accounts import views

urlpatterns = [
    path('signup/', views.signup.as_view(), name='signup'),
    path('login/', views.login.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
]