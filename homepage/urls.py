from django.urls import path

from homepage.views.about_us_view import AboutUsView
from homepage.views.blog_view import BlogsView, BlogDetails
from homepage.views.case_study_view import CaseStudyDetails
from homepage.views.contact_us_view import ContactUs
from homepage.views.index_view import IndexView
from homepage.views.product_view import ProductsView

app_name= 'homepage'

urlpatterns= [
    path('', IndexView.as_view(), name="index_url"),
    path('about-us/', AboutUsView.as_view(), name="about_us_url"),
    path('product/', ProductsView.as_view(), name="product_url"),

    path('blog/', BlogsView.as_view(), name="blog_url"),
    path('blog-details/<str:slug>/', BlogDetails.as_view(), name="blog_details_url"),

    path('contact-us/', ContactUs.as_view(), name="contact_us_url"),

    path('case-study/<str:slug>/', CaseStudyDetails.as_view(), name="case_study_details_url")

]