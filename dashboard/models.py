import email
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from dashboard.utils import SlugGeneratorMixin

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
WEB = 1
APP = 2
UI_UX = 3
PROJECT_TYPE = (
    (WEB, 'Web'),
    (APP, 'App'),
    (UI_UX, 'Ui/Ux'),

)
BELOW_3000 = 1
_3000_TO_10000 = 2
_10000_TO_20000 = 3
_20000_TO_30000 = 4
_30000_TO_40000 = 5
_40000_TO_50000 = 6
OVER_50000 = 7

BUDGET = (
    (BELOW_3000, 'Below $3000'),
    (_3000_TO_10000, '$3000 to $10000'),
    (_10000_TO_20000, '$10000 to $20000'),
    (_20000_TO_30000, '$20000 to $30000'),
    (_30000_TO_40000, '$30000 to $40000'),
    (_40000_TO_50000, '$40000 to $50000'),
    (OVER_50000, 'Over $50000'),
)
FULL_TIME = 1
REMOTE =2 
PART_TIME = 3
APPLICENT_STATUS = (
    (FULL_TIME, 'Full Time'),
    (REMOTE, 'Remote'),
    (PART_TIME, 'Part Time'),

)
PENDING = 1
CONTACTED = 2
LETS_TAlK_STATUS = (
    (PENDING, 'Pending'),
    (CONTACTED, 'Contacted'),
)


class Technologies(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='technologies')


class WhatProjectHaveWeDone(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='project_done/')
    technology = models.TextField()
    slug = models.SlugField(null=True, blank=True)
    project_type = models.PositiveSmallIntegerField(choices=PROJECT_TYPE)

    @property
    def split_technology(self):
        return self.technology.split(',')        


class CaseStudyDetails(models.Model):
    project_we_have_done = models.OneToOneField(WhatProjectHaveWeDone, related_name='case_study_details',
                                                on_delete=models.CASCADE)
    case_study_about = models.TextField(null=True, blank=True)
    case_study_image = models.ImageField(upload_to='case_study/', null=True, blank=True)
    client_requirement = models.TextField(null=True, blank=True)
    how_we_build_it = models.TextField(null=True, blank=True)
    how_we_build_image = models.ImageField(upload_to='how_we_build/', null=True, blank=True)
    technology = models.ManyToManyField(Technologies)


class KeyFeature(models.Model):
    case_study_details = models.ForeignKey(CaseStudyDetails, related_name='key_features',
                                           on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='key_feature')


class Subscribe(models.Model):
    email = models.CharField(max_length=200)


class BlogAuthor(models.Model):
    name = models.CharField(max_length=100)
    qualification = models.TextField()
    image = models.ImageField(upload_to='blog/author/')

    def __str__(self):
        return str(self.name)
  

class BlogCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null= True)

    def __str__(self):
        return str(self.name)


class Blog(models.Model):
    blog_author = models.ForeignKey(BlogAuthor, null=True, related_name='blogs', on_delete=models.CASCADE)
    blog_category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null= True)
    slug = models.SlugField(null=True, allow_unicode=True, blank=True)
    title = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='blog/')
    tags = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return str(self.blog_author.name) + '-' + str(self.title)

    def get_absolute_url(self):
        return


class LetsTalk(models.Model):
    name = models.CharField(max_length= 200, null= True)
    email = models.CharField(null= True, max_length= 100)
    phone_number = models.CharField(max_length= 30)
    budget = models.PositiveSmallIntegerField( choices= BUDGET)
    message = models.TextField(null= True)
    status = models.PositiveSmallIntegerField( choices= LETS_TAlK_STATUS, default=PENDING)


@receiver(post_save, sender=BlogCategory)
@receiver(post_save, sender=Blog)
@receiver(post_save, sender=WhatProjectHaveWeDone)
def slug_generator(sender, instance, created, **kwargs):
    if created and sender == WhatProjectHaveWeDone:
        CaseStudyDetails.objects.create(project_we_have_done=instance)
    if instance.slug is None:
        slug_object = SlugGeneratorMixin()
        slug = slug_object.unique_slug_generator(instance)
        instance.slug = slug
        instance.save()


class HandleBlog(models.Model):
    top_4_blog = models.ManyToManyField(Blog)
    highlight_blog= models.ForeignKey(Blog, related_name='handle_blog',on_delete= models.SET_NULL, null= True)


class ApplyForThisPosition(models.Model):
    title = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    upload_cv = models.FileField(upload_to='apply_for_this_position/')
    current_opportunities = models.ForeignKey("CurrentOpportunities",on_delete=models.CASCADE, related_name='apply_for_positions')


class CurrentOpportunities(models.Model):
    title = models.CharField(max_length=100)
    applicant_type = models.PositiveSmallIntegerField( choices= APPLICENT_STATUS, default=FULL_TIME)
    number_of_vacancy = models.CharField(max_length=50)
    deadline = models.DateTimeField()
    description = models.TextField()
    



    