from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from michellemark.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('my-admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('', include('public_pages.urls')),
]
