from django.urls import path
from website.views import home, contact, about, Appoint, blog, blogsingle, department, price

urlpatterns = [
    path('',home,name='home'),
    path('contact.html',contact,name='contact'),
    path('about.html',about,name='about'),
    path('appointment.html', Appoint.as_view(), name='appointment'),
    path('blog.html',blog,name='blog'),
    path('blogsingle.html',blogsingle,name='blogsingle'),
    path('department.html',department,name='department'),
    path('pricing.html',price,name='price'),
]
