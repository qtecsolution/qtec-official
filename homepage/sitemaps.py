from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from dashboard.models import Blog


class StaticViewSitemap(Sitemap):
    changefreq = "daily"

    def items(self):
        return ['homepage:index_url', 'homepage:about_us_url']

    def location(self, item):
        return reverse(item)


class BlogSitemap(Sitemap):
    changefreq = "daily"

    def items(self):
        return Blog.objects.all().values("slug")

    def location(self, obj):
        obj = obj.get("slug", "")
        return reverse('homepage:blog_details_url', kwargs={'slug': obj})
