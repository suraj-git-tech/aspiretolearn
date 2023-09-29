from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('single-blog/<int:post_id>/',views.single_blog, name='single-blog'),
    path('single-blog/',views.single_blog, name='single-blog'),
    path('category/',views.category, name='category'),
    path('category/<int:cat_id>/',views.category, name='category'),
    path('contact/',views.contact, name='contact'),
    path('about/',views.about, name='about'),
    path('search_result/',views.search_result, name='search_result'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('log-in/', views.log_in, name='log_in'),
]
