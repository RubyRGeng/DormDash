from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [('accounts.views',
url(r'^view_profile/$', 'view_profile', name ='view_profile'),
url(r'^view_profile/edit_profile/$', 'edit_profile', name ='edit_profile'))
]
urlpatterns = [
    path('createaccount/', views.createaccount),
    path('login/', views.login),
    path('admin/', admin.site.urls),
]
