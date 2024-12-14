from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_form, name='blog_form'),
    # path('blog', views.blog_form, name='blog_form'),
    path('ajax_call', views.ajax_call, name='ajax_call'),

]