from . import views
from django.urls import path
urlpatterns = [

    path('login', views.Login , name = "login" ),
    path('signup', views.signup ,name= "signup" ),
    path('logout', views.LogoutView.as_view() , name = 'logout'),
]