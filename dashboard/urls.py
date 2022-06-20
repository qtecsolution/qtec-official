from django.urls import path
from dashboard.views.already_done_view import AlreadyDoneView, CaseStudyEditView
from dashboard.views.blog_view import BlogView, HandleBlogView

from dashboard.views.dashboard import DashboardView
from dashboard.views.lets_talk_view import LetsTalkView
from dashboard.views.subscribe_view import SubscribeView
from dashboard.views.technologies_view import TechnologiesView

app_name= 'dashboard'

urlpatterns= [
    path('dashboard/', DashboardView.as_view(), name= 'dashboard_url'),

    # already-done
    path('already-done/', AlreadyDoneView.as_view(), name= 'already_done_url'),
    path('already-done-delete/', AlreadyDoneView.as_view(), name= 'delet_what_done_url'),
    path('already-done-edit/', AlreadyDoneView.as_view(), name= 'edit_what_project_done_url'),
    path('already-done-save/', AlreadyDoneView.as_view(), name= 'save_what_done_url'),
    path('case-study-edit/<int:id>/', CaseStudyEditView.as_view(), name= 'case_study_edit_url'),

    # subscribe
    path('subscribe/', SubscribeView.as_view(), name= 'subscribe_url'),

    # technologies
    path('technologies/', TechnologiesView.as_view(), name= 'technologies_url'),
    path('technologies-save/', TechnologiesView.as_view(), name= 'save_technologies_url'),
    path('technologies-delete/', TechnologiesView.as_view(), name= 'delet_technologies_url'),    

     # blog
    path('blog-list/', BlogView.as_view(), name="blog_blog_list_url"),
    path('blog-list-save/', BlogView.as_view(), name="save_blog_url"),
    path('blog-list-edit/', BlogView.as_view(), name="edit_blog_url"),
    path('blog-list-delete/', BlogView.as_view(), name="delet_blog_row_url"),
    path('handle-blog/', HandleBlogView.as_view(), name="handle_blog_url"),

    # LetsTalk
    path('lets-talk/', LetsTalkView.as_view(), name="lets_talk_url"),
    path('lets-talk-delete/', LetsTalkView.as_view(), name="delet_lets_talk_url"),
    path('lets-talk-status/', LetsTalkView.as_view(), name="lets_talk_status_change_url"),
]