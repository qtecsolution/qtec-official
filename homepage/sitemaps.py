from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from dashboard.models import *


class StaticViewSitemap(Sitemap):
    changefreq = "daily"

    def items(self):
        return [
            'homepage:index_url',
            'homepage:about_us_url',
            'homepage:product_url',
            'homepage:case_study_list_url',
            'homepage:contact_us_url',
            'homepage:lets_talk_subscribe_save_url',
            'homepage:career_url',
            'homepage:apply_for_job_url',
            'homepage:service_url',
            'homepage:all_blog_url',
            'homepage:blog_url',
        ]

    def location(self, item):
        return reverse(item)


class BlogSitemap(Sitemap):
    changefreq = "daily"

    def items(self):
        return Blog.objects.all().values("slug")

    def location(self, obj):
        obj = obj.get("slug", "")
        return reverse('homepage:blog_details_url', kwargs={'slug': obj})


class WhatProjectHaveWeDoneSitemap(Sitemap):
    changefreq = "daily"

    def items(self):
        return WhatProjectHaveWeDone.objects.all().values("slug")

    def location(self, obj):
        obj = obj.get("slug", "")
        return reverse('homepage:case_study_details_url', kwargs={'slug': obj})


class CurrentOpportunitiesSitemap(Sitemap):
    changefreq = "daily"

    def items(self):
        return CurrentOpportunities.objects.all().values("slug")

    def location(self, obj):
        obj = obj.get("slug", "")
        return reverse('homepage:career_details_url', kwargs={'slug': obj})


class ServiceDetailsProjectSitemap(Sitemap):
    changefreq = "daily"

    def items(self):
        return ServiceDetailsProject.objects.all().values("slug")

    def location(self, obj):
        obj = obj.get("slug", "")
        return reverse('homepage:service_details_url', kwargs={'slug': obj})


class TechnologiesSitemap(Sitemap):
    changefreq = "daily"

    def items(self):
        return Technologies.objects.all().values("slug")

    def location(self, obj):
        obj = obj.get("slug", "")
        return reverse('homepage:technologies_url', kwargs={'slug': obj})
