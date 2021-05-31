from django.urls import path
from .import views

urlpatterns=[
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('editprofile/', views.editprofile, name="editprofile"),
    path('ratecourse/',views.ratecourse,name="ratecourse"),
    path('',views.home,name='home'),
]