import random
import string

from django.utils.text import slugify
from langdetect import detect


class SlugGeneratorMixin(object):

    def random_string_generator(self, size=10, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def unique_slug_generator(self, instance, new_slug=None):
        Klass = instance.__class__
        klass_name = Klass.__name__
        if new_slug is not None:
            slug = new_slug
        else:
            if klass_name == 'WhatProjectHaveWeDone' or klass_name == 'BlogCategory':
                slug = slugify(instance.name).replace("&", "and")
            if klass_name == 'Blog' or klass_name == 'CurrentOpportunities' or klass_name == 'Technologies':
                if detect(instance.title) == 'en':
                    slug = slugify(instance.title).replace("&", "and")
                else:
                    slug = instance.title.replace(" ","-")

        qs_exists = Klass.objects.filter(slug=slug).exists()

        if qs_exists:
            new_slug = "{slug}-{randstr}".format(
                slug=slug, randstr=self.random_string_generator(size=4))
            return self.unique_slug_generator(instance, new_slug=new_slug)
        return slug
