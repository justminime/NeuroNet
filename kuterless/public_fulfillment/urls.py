from django.conf.urls import patterns, url
from public_fulfillment import views


urlpatterns = patterns('',
#/sign_up
    url(r'^$', views.about, name='about'),
    
    url(r'^register/$', views.sign_up, name='sign_up'),                       
    url(r'^update_profile/$', views.update_profile, name='update_profile'),                       
)



    
    
    