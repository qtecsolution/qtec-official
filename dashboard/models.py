from datetime import datetime
from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from dashboard.utils import SlugGeneratorMixin
from langdetect import detect

from .filters.youtube_link_filters import extract_video_id

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
UNSEEN = 1
SEEN = 2
PENDING = 3
SELECTED = 4
REJECTED = 5

APPLY_STATUS = (
    (UNSEEN, 'Unseen'),
    (SEEN, 'Seen'),
    (PENDING, 'Pending'),
    (SELECTED, 'Selected'),
    (REJECTED, 'Rejected'),

)
FULL_TIME = 1
REMOTE = 2
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

OPT_IN = 0
OPT_OUT = 1
SUBSCRIBE_STATUS = (
    (OPT_IN, 'opt in'),
    (OPT_OUT, 'opt out')
)
ACTIVE = 0
CLOSED = 1
ACTIVE_STATUS = (
    (ACTIVE, 'Active'),
    (CLOSED, 'Closed')
)

STATUS_TYPE = (
    ('PENDING', 'Pending'),
    ('PROCCESSING', 'Proccessing'),
    ('CONFIRMED', 'Confirmed'),
    ('REJECTED', 'Rejected')
)


class Technologies(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='technologies')
    technology_details_title = models.CharField(max_length=100)
    technology_detail_description = models.TextField()
    technology_detail_thumbnail = models.ImageField(
        upload_to='technologies/', null=True, blank=True)
    why_this_technologies_title = models.CharField(max_length=100)
    why_this_technologies_description = models.TextField()
    why_this_technologies_image = models.ImageField(
        upload_to='technologies/', null=True, blank=True)
    why_choice_title = models.CharField(max_length=200)
    why_choice_description = models.TextField()
    why_choice_image = models.ImageField(
        upload_to='technologies/', null=True, blank=True)
    technology_features = models.ManyToManyField(
        "TechnologyFeatures", related_name="technologies")
    display = models.BooleanField(default=True)


class TechnologyFeatures(models.Model):
    title = models.CharField(max_length=200)
    heading = models.CharField(max_length=200)
    description = models.TextField()


class WhatProjectHaveWeDone(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='project_done/')
    video = models.CharField(max_length=500, null=True, blank=True)
    technology = models.ManyToManyField(Technologies)
    slug = models.SlugField(null=True, blank=True)
    project_type = MultiSelectField(choices=PROJECT_TYPE)
    priority = models.PositiveSmallIntegerField(default=0, null=True)
    display = models.BooleanField(default=True)
    homepage = models.BooleanField(default=True)
    meta_description = models.TextField(null=True)
    keywords = models.TextField(null=True)

    @property
    def split_technology(self):
        return self.technology.split(',')

    @property
    def video_id(self):
        if self.video:
            return extract_video_id(self.video)
        return None

    @video_id.setter
    def video_id(self, value):
        if value:
            self.video = f'https://www.youtube.com/embed/{value}'
        else:
            self.video = None

    def save(self, *args, **kwargs):
        if self.video:
            video_id = extract_video_id(self.video)
            if video_id:
                self.video = f'https://www.youtube.com/embed/{video_id}'
            else:
                self.video = None

        super().save(*args, **kwargs)


class CaseStudyDetails(models.Model):
    project_we_have_done = models.OneToOneField(WhatProjectHaveWeDone, related_name='case_study_details',
                                                on_delete=models.CASCADE)
    case_study_about = models.TextField(null=True, blank=True)
    case_study_image = models.ImageField(
        upload_to='case_study_image/', null=True, blank=True)
    client_requirement = models.TextField(null=True, blank=True)
    requirements_thumbnail = models.ImageField(
        upload_to='case_study/', null=True, blank=True)
    how_we_build_it = models.TextField(null=True, blank=True)
    how_we_build_image = models.ImageField(
        upload_to='how_we_build/', null=True, blank=True)
    technology = models.ManyToManyField(Technologies)
    meta_description = models.TextField(null=True)
    keywords = models.TextField(null=True)


class KeyFeature(models.Model):
    case_study_details = models.ForeignKey(CaseStudyDetails, related_name='key_features',
                                           on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='key_feature')


class Subscribe(models.Model):
    email = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now)
    status = models.PositiveSmallIntegerField(
        choices=SUBSCRIBE_STATUS, default=OPT_IN)


class BlogAuthor(models.Model):
    name = models.CharField(max_length=100)
    qualification = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='blog/author/', blank=True, null=True)

    def __str__(self):
        return str(self.name)


class BlogCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=True)

    def __str__(self):
        return str(self.name)


class Blog(models.Model):
    blog_author = models.ForeignKey(
        BlogAuthor, null=True, related_name='blogs', on_delete=models.CASCADE)
    blog_category = models.ForeignKey(
        BlogCategory, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(
        null=True, allow_unicode=True, unique=True, blank=True)
    title = models.TextField()
    description = models.TextField()
    og_description = models.TextField(null=True)
    meta_description = models.TextField(null=True)
    keywords = models.TextField(null=True)
    image = models.ImageField(upload_to='blog/')
    thumbnail = models.ImageField(
        upload_to='blog/thumbnail/', null=True, blank=True)
    alt_text = models.CharField(max_length=250, null=True, default=True)
    tags = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    updated_at = models.DateField(auto_now=True, null=True)
    display = models.BooleanField(default=True)
    url = models.CharField(max_length=250, null=True)

    def __str__(self):
        return str(self.blog_author.name) + '-' + str(self.title)

    def get_absolute_url(self):
        return


class LetsTalk(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(null=True, max_length=100)
    phone_number = models.CharField(max_length=30)
    budget = models.PositiveSmallIntegerField(choices=BUDGET)
    message = models.TextField(null=True)
    status = models.PositiveSmallIntegerField(
        choices=LETS_TAlK_STATUS, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)


class HandleBlog(models.Model):
    top_4_blog = models.ManyToManyField(Blog)
    highlight_blog = models.ForeignKey(
        Blog, related_name='handle_blog', on_delete=models.CASCADE, null=True)


class ApplyForThisPosition(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    upload_cv = models.FileField(upload_to='apply_for_this_position/')
    current_opportunities = models.ForeignKey("CurrentOpportunities", on_delete=models.CASCADE,
                                              related_name='apply_for_positions')
    status = models.PositiveSmallIntegerField(
        choices=APPLY_STATUS, default=UNSEEN)
    date = models.DateTimeField(auto_now_add=True)


class CurrentOpportunities(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='opportunities/', null=True)
    slug = models.SlugField(null=True, allow_unicode=True, blank=True)
    applicant_type = models.PositiveSmallIntegerField(
        choices=APPLICENT_STATUS, default=FULL_TIME)
    number_of_vacancy = models.PositiveIntegerField()
    deadline = models.DateField()
    description = models.TextField()
    display = models.BooleanField(default=True)

    @property
    def get_status(self):
        today = datetime.now().date()
        if today > self.deadline:
            return CLOSED
        else:
            return ACTIVE


class ServiceDetailsProject(models.Model):
    slug = models.SlugField(null=True)
    project = models.ManyToManyField(WhatProjectHaveWeDone)


@receiver(post_save, sender=Technologies)
@receiver(post_save, sender=CurrentOpportunities)
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


class TeamMembers(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='team_members/')
    designation = models.CharField(max_length=100)
    github = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    gmail = models.EmailField(max_length=100)
    priority = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return self.name


class LegalTeamMembers(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='team_members/')
    designation = models.CharField(max_length=100)
    github = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    gmail = models.EmailField(max_length=100)
    priority = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return self.name


class MarketingTeamMembers(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='team_members/')
    designation = models.CharField(max_length=100)
    github = models.CharField(max_length=100, null=True, blank=True)
    linkedin = models.CharField(max_length=100, null=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    gmail = models.EmailField(max_length=100)
    priority = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return self.name


class OurGallery(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    primary_image = models.ImageField(upload_to='about-gallery/')
    secondary_image = models.ImageField(upload_to='about-gallery/')
    priority = models.PositiveSmallIntegerField()


class ClientImage(models.Model):
    image = models.ImageField(upload_to='home-client/')


class HomeClients(models.Model):
    title = models.CharField(max_length=250)
    clent_image = models.ManyToManyField(ClientImage)


class WhatPeopleSay(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=250)
    image = models.ImageField(upload_to='what-people-say/')
    description = models.TextField()
    priority = models.PositiveSmallIntegerField()


class Service(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class AugmantationBudget(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Augmantation Budget'
        verbose_name_plural = 'Augmantation Budgets'


class AugmentationService(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    services = models.ForeignKey(
        Service, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(
        max_length=100, choices=STATUS_TYPE, default='PENDING')
    budget = models.ForeignKey(
        AugmantationBudget, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Augmentation Service'
        verbose_name_plural = 'Augmentation Services'


class BookDownloader(models.Model):
    user_name = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField()

    def __str__(self):
        return self.user_name


class YouTubeVideo(models.Model):
    # Page constants
    HOME = 1
    ABOUT_US = 2
    SERVICES = 3
    TECHNOLOGIES = 4
    PROJECTS = 5
    CLIENTS = 6
    CONTACT_US = 7
    OUR_TEAM = 8
    LEGAL_TEAM = 9
    OUR_GALLERY = 10
    WHAT_PEOPLE_SAY = 11
    CURRENT_OPPORTUNITIES = 12
    AUGMENTATION_SERVICES = 13
    BLOG = 14

    PAGE_CHOICES = [
        (HOME, 'Home'),
        (ABOUT_US, 'About Us'),
        (SERVICES, 'Services'),
        (TECHNOLOGIES, 'Technologies'),
        (PROJECTS, 'Projects'),
        (CLIENTS, 'Clients'),
        (CONTACT_US, 'Contact Us'),
        (OUR_TEAM, 'Our Team'),
        (LEGAL_TEAM, 'Legal Team'),
        (OUR_GALLERY, 'Our Gallery'),
        (WHAT_PEOPLE_SAY, 'What People Say'),
        (CURRENT_OPPORTUNITIES, 'Current Opportunities'),
        (AUGMENTATION_SERVICES, 'Augmentation Services'),
        (BLOG, 'Blog'),
    ]

    video_url = models.URLField("YouTube Video URL", max_length=500)
    page = models.PositiveSmallIntegerField(choices=PAGE_CHOICES, default=HOME)
    display = models.BooleanField(default=True)

    def extract_video_id(self):
        """
        Extracts the YouTube video ID from the video_url.
        """
        import re
        patterns = [
            r'youtu\.be/(?P<id>[a-zA-Z0-9_-]+)',  # Short URL format
            r'youtube\.com/watch\?v=(?P<id>[a-zA-Z0-9_-]+)',  # Full URL format
            r'youtube\.com/embed/(?P<id>[a-zA-Z0-9_-]+)',  # Embed URL format
        ]
        for pattern in patterns:
            match = re.search(pattern, self.video_url)
            if match:
                return match.group('id')
        return None

    @property
    def embed_url(self):
        """
        Returns the embeddable YouTube link.
        """
        video_id = self.extract_video_id()
        if video_id:
            return f"https://www.youtube.com/embed/{video_id}"
        return None

    def __str__(self):
        return f"{self.get_page_display()}: {self.video_url}"
