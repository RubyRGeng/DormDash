from django.urls import path
from . import views
from .views import profile, restaurant_list
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from DormDashApp.views import logoutUser


# URLConf
urlpatterns = [
    path('createaccount/', views.createaccount),
    path('', views.loginUser),
    path('restaurant_list/', views.restaurant_list, name="restaurant_list"),
    path('logout/', views.logoutUser, name="logout"),
    path('login/', views.loginUser, name="login"),
    path('profile/', profile, name='users-profile'),
    path('driverorders/',views.driverorders, name='driverorders'),
    path('orderdetails/',views.orderdetails, name='orderdetails'),


]
urlpatterns += staticfiles_urlpatterns()