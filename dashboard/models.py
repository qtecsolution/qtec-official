from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


TEXT = 1
TEXT_WITH_VIDEO = 2
BLOG_TYPE = (
    (TEXT, 'text'),
    (TEXT_WITH_VIDEO, 'text with video')
)


TRANDY = 1
BLOG_CONDITION_TYPE = (
    (TRANDY, 'TRANDY'),
)


class WhatProjectHaveWeDone(models.Model):
    name = models.CharField(max_length=50)


class Subscribe(models.Model):
    email= models.CharField(max_length= 200)


class BlogAuthor(models.Model):
    name = models.CharField(max_length=100)
    institute = models.CharField(max_length=250, null=True)
    biography = models.TextField(null=True)
    designation = models.CharField(max_length=50)
    qualification = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='blog/author/')

    def __str__(self):
        return str(self.name)


class BlogRootCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class BlogSubCategory(models.Model):
    root = models.ForeignKey(BlogRootCategory, related_name='sub_categories', on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class SlugGeneratorMixin:
    pass


@receiver(post_save, sender=BlogSubCategory)
def create_video_blog(sender, instance, created, **kwargs):
    if created:
        if instance.slug is None:
            slug_object = SlugGeneratorMixin()
            slug = slug_object.unique_slug_generator(instance)
            instance.slug = slug
            instance.save()


class Blog(models.Model):
    blog_author = models.ForeignKey(BlogAuthor, null=True, related_name='blogs', on_delete=models.CASCADE)
    category = models.ForeignKey(BlogSubCategory, null=True, related_name='blogs', on_delete=models.CASCADE)
    slug = models.SlugField(null=True, allow_unicode=True, blank=True)
    title = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='blog/')
    blog_type = models.PositiveSmallIntegerField(choices=BLOG_TYPE)
    blog_condition = models.PositiveSmallIntegerField(choices=BLOG_CONDITION_TYPE, null=True, blank=True)
    tags = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return str(self.blog_author.name) + '-' + str(self.title)
