from django.urls import path
from homepage.views.Error_404_view import Error_404

from homepage.views.about_us_view import AboutUsView
from homepage.views.blog_view import BlogsView, BlogDetails, AllBlogView
from homepage.views.career_view import CareerView, CareerDetailsView
from homepage.views.case_study_view import CaseStudyDetailsView
from homepage.views.contact_us_view import ContactUs
from homepage.views.index_view import IndexView
from homepage.views.product_view import ProductsView
from homepage.views.service_view import ServiceView, ServiceDetailsView
from homepage.views.technologies_view import TechnologiesView

app_name= 'homepage'

urlpatterns= [
    path('', IndexView.as_view(), name="index_url"),
    path('about-us/', AboutUsView.as_view(), name="about_us_url"),
    path('products/', ProductsView.as_view(), name="product_url"),

    path('all-blog/', AllBlogView.as_view(), name="all_blog_url"),
    path('blogs/', BlogsView.as_view(), name="blog_url"),
    path('<str:slug>/', BlogDetails.as_view(), name="blog_details_url"),

    path('contact-us/', ContactUs.as_view(), name="contact_us_url"),

    path('case-study/<str:slug>/', CaseStudyDetailsView.as_view(), name="case_study_details_url"),

    path('lets-talk-subscribe-save/', ContactUs.as_view(), name="lets_talk_subscribe_save_url"),

    path('career/', CareerView.as_view(), name="career_url"),
    path('career/<str:slug>/', CareerDetailsView.as_view(), name="career_details_url"),

    path('apply/job/', CareerDetailsView.as_view(), name="apply_for_job_url"),

    path('services/', ServiceView.as_view(), name="service_url"),
    path('service-details/<str:slug>/', ServiceDetailsView.as_view(), name="service_details_url"),

    path('technologies/<str:slug>/', TechnologiesView.as_view(), name="technologies_url"),

    path('error_404/', Error_404.as_view(), name="error_url"),




]
