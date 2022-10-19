
import random
import string
from utils.code_prefix import *
from utils.signatures import make_random_digits
from django.template.defaultfilters import slugify

class UniqueSlugCodeMixin(object):

    @staticmethod
    def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def unique_slug_generator(self, instance, new_slug = None):
        Klass = instance.__class__
        klass_name = Klass.__name__
        if new_slug is not None:
            slug = new_slug
        else:
            title = None
            if klass_name == 'Channel':
                title = instance.name
            elif klass_name == "VideoContent":
                title = instance.title
            slug = slugify(title)

        qs_exists = Klass.objects.filter(slug = slug).exists()
        if qs_exists:
            new_slug = "{slug}-{randstr}".format(slug = slug, randstr = make_random_digits(6))
            return self.unique_slug_generator(instance, new_slug = new_slug)
        return slug


    def unique_code_generator(self, instance, new_code = None):
        Klass = instance.__class__

        if new_code is not None:
            code = new_code
        else:
            code = random.randint(100000001, 999999999)
        qs_exists = Klass.objects.filter(slug = code).exists()
        if qs_exists:
            new_code = random.randint(100000001, 999999999)
            return self.unique_code_generator(instance, new_code = new_code)
        return code
