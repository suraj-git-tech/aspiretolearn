from django.contrib import admin
from django.urls import include, path
# from allauth.socialaccount.providers.oauth2.views import OAuth2LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/', include(('blogs.urls', 'blogs'))),
    path('accounts/', include('django.contrib.auth.urls')),
]
