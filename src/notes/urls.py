from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact_page, name='contact'),
    path('subject/<pk>', views.posts_page, name='posts'),
    path('subject/<subject>/answer/<pk>', views.answer_page, name='answer'),
]