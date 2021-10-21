from django.urls import path
from . import views
# URLConf
urlpatterns = [
    path('createaccount/', views.createaccount),
    path('login/', views.login)
]