from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from DormDashApp.views import logoutUser


# URLConf
urlpatterns = [
    path('createaccount/', views.createaccount),
    path('', views.login),
    path('restaurant_list/', views.restaurant_list),
    path('logout/', views.logoutUser, name="logout"),
    path('login/', views.login, name="login")


]
urlpatterns += staticfiles_urlpatterns()