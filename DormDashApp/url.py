from django.conf.urls import patterns, url

urlpatterns = patterns('accounts.views',
url(r'^view_profile/$', 'view_profile', name ='view_profile'),
url(r'^view_profile/edit_profile/$', 'edit_profile', name ='edit_profile')
