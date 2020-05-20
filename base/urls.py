from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from django.contrib.sitemaps import GenericSitemap # new
from django.contrib.sitemaps.views import sitemap # new

from posts.models import Post

info_dict = {
    'queryset': Post.objects.all(),
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('user/', include('users.urls')),   
    path('user/', include('django.contrib.auth.urls')),

    path('sitemap.xml/', sitemap,
        {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
        name='django.contrib.sitemaps.views.sitemap'),
    
]

