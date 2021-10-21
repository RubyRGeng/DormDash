from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# URLConf
urlpatterns = [
    path('createaccount/', views.createaccount),
    path('', views.login),

]
urlpatterns += staticfiles_urlpatterns()