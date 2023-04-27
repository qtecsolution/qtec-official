from cgitb import handler
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from homepage.sitemaps import *
sitemaps = {
    'static': StaticViewSitemap,
    'blogs': BlogSitemap,
    'case_study': WhatProjectHaveWeDoneSitemap,
    'carrer': CurrentOpportunitiesSitemap,
    'service': ServiceDetailsProjectSitemap,
    'tech': TechnologiesSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls', namespace="homepage")),
    path('dashboard/', include('dashboard.urls', namespace="dashboard")),
    path('__debug__/', include('debug_toolbar.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'qtec_official.404error.handler404'
handler500 = 'qtec_official.404error.handler500'
