from django.urls import path
from dashboard.views.already_done_view import AlreadyDoneView, CaseStudyEditView, KeyFeatureView
from dashboard.views.authenticate_view import AuthenticationView
from dashboard.views.blog_view import BlogAuthorView, BlogCategoryView, BlogView, HandleBlogView
from dashboard.views.career_view import ApplyForThisPositionView, CurrentOpportunitiesView

from dashboard.views.dashboard import DashboardView
from dashboard.views.home_clients_view import HomeClientsView
from dashboard.views.lets_talk_view import LetsTalkView
from dashboard.views.our_gallery_view import OurGalleryView
from dashboard.views.subscribe_view import SubscribeView
from dashboard.views.team_members_view import TeamMembersView
from dashboard.views.technologies_view import TechnologiesView
from dashboard.views.what_people_say_view import WhatPeopleSayView

app_name= 'dashboard'

urlpatterns= [

    path('login/', AuthenticationView.as_view(), name='dashboard_login_url'),
    path('logout/', AuthenticationView.as_view(), name="logout_dashboard_url"),

    path('', DashboardView.as_view(), name= 'dashboard_url'),

    # already-done
    path('already-done/', AlreadyDoneView.as_view(), name= 'already_done_url'),
    path('already-done-delete/', AlreadyDoneView.as_view(), name= 'delete_what_done_url'),
    path('already-done-edit/', AlreadyDoneView.as_view(), name= 'edit_what_project_done_url'),
    path('already-done-save/', AlreadyDoneView.as_view(), name= 'save_what_done_url'),
    path('already-done-status/', AlreadyDoneView.as_view(), name= 'status_what_done_url'),

    path('case-study-edit/<int:id>/', CaseStudyEditView.as_view(), name= 'case_study_edit_url'),
    path('case-study-image-delete/', CaseStudyEditView.as_view(), name= 'case_study_image_delete_url'),
    path('key-feature/<int:id>/', KeyFeatureView.as_view(), name= 'key_feature_url'),
    path('key-feature-update/<int:id>/', KeyFeatureView.as_view(), name= 'update_key_feature_url'),
    path('key-feature-delete/<int:id>/', KeyFeatureView.as_view(), name= 'delete_key_feature_url'),
   

    # subscribe
    path('subscribe/', SubscribeView.as_view(), name= 'subscribe_url'),
    path('subscribe-status/', SubscribeView.as_view(), name= 'subscriber_status_change_url'),

    # technologies
    path('technologies/', TechnologiesView.as_view(), name= 'technologies_url'),
    path('technologies-save/', TechnologiesView.as_view(), name= 'save_technologies_url'),
    path('technologies-delete/', TechnologiesView.as_view(), name= 'delete_technologies_url'), 
    path('technologies-features/', TechnologiesView.as_view(), name= 'save_technologies_features_url'),  
    path('technologies-update/<int:id>/', TechnologiesView.as_view(), name= 'update_technologies_url'), 
    path('technologies-status/', TechnologiesView.as_view(), name= 'change_status_technologies_url'), 

     # blog
    path('blog-list/', BlogView.as_view(), name="blog_blog_list_url"),
    path('blog-list-save/', BlogView.as_view(), name="save_blog_url"),
    path('blog-list-edit/', BlogView.as_view(), name="edit_blog_url"),
    path('blog-list-delete/', BlogView.as_view(), name="delete_blog_row_url"),
     path('blog-list-display/', BlogView.as_view(), name="display_blog_row_url"),

    path('handle-blog/', HandleBlogView.as_view(), name="handle_blog_url"),

    path('blog-author/', BlogAuthorView.as_view(), name="blog_blog_author_url"),
    path('blog-author-save/', BlogAuthorView.as_view(), name="save_blog_blog_author_url"),
    path('blog-author-delete/', BlogAuthorView.as_view(), name="delete_blog_blog_author_url"),
    path('blog-author-edit/', BlogAuthorView.as_view(), name="edit_blog_blog_author_url"),
    
    path('blog-blog-category/', BlogCategoryView.as_view(), name="blog_blog_category_url"),
    path('blog-blog-category-save/', BlogCategoryView.as_view(), name="save_blog_category_url"),
    path('blog-blog-category-delete/', BlogCategoryView.as_view(), name="delete_blog_blog_category_url"),
    path('blog-blog-category-update/', BlogCategoryView.as_view(), name="edit_blog_blog_category_url"),

    # LetsTalk
    path('lets-talk/', LetsTalkView.as_view(), name="lets_talk_url"),
    path('lets-talk-delete/', LetsTalkView.as_view(), name="delete_lets_talk_url"),
    path('lets-talk-status/', LetsTalkView.as_view(), name="lets_talk_status_change_url"),

    # opportunities
    path('current-opportunities/', CurrentOpportunitiesView.as_view(), name="current_opportunities_url"),
    path('current-opportunities-save/', CurrentOpportunitiesView.as_view(), name="save_current_opportunities_url"),
    path('current-opportunities-edit/', CurrentOpportunitiesView.as_view(), name="current_opportunities_edit_url"),
    path('current-opportunities-delete/', CurrentOpportunitiesView.as_view(), name="delete_current_opportunities_url"),
    path('current-opportunities-status/', CurrentOpportunitiesView.as_view(), name="change_status_current_opportunities_url"),
    path('current-opportunities-display/', CurrentOpportunitiesView.as_view(), name="display_current_opportunities_url"),
    
    path('career-apply-for-this-position/', ApplyForThisPositionView.as_view(), name="apply_for_this_position_url"),
    path('career-apply-for-this_position-satus/', ApplyForThisPositionView.as_view(), name="apply_for_this_position_status_url"),
    path('career-apply-for-this-position-delete/', ApplyForThisPositionView.as_view(), name="apply_for_this_position_delete_url"),
    

   
    path('team-members/', TeamMembersView.as_view(), name="team_members_url"),
    path('team-members-delete/', TeamMembersView.as_view(), name="delete_team_member_url"),
    path('team-members-create/', TeamMembersView.as_view(), name="save_team_member_url"),
    path('team-members-update/<int:id>/', TeamMembersView.as_view(), name="update_team_member_url"),
    

    path('our-gallery/', OurGalleryView.as_view(), name="our_gallery_url"),
    path('our-gallery-create/', OurGalleryView.as_view(), name="save_our_gallery_url"),
    path('our-gallery-update/<int:id>/', OurGalleryView.as_view(), name="update_our_gallery_url"),
    path('our-gallery-delete/', OurGalleryView.as_view(), name="delete_our_gallery_url"),

    path('home-clients/', HomeClientsView.as_view(), name="home_clients_url"),
    path('home-clients-image-delete/', HomeClientsView.as_view(), name="home_clients_image_url"),

    path('what-people-say/', WhatPeopleSayView.as_view(), name="what_people_say_url"),
    path('what-people-say-create/', WhatPeopleSayView.as_view(), name="create_what_people_say_url"),
    path('what-people-say-update/<int:id>', WhatPeopleSayView.as_view(), name="update_what_people_say_url"),
    path('what-people-say-delete/', WhatPeopleSayView.as_view(), name="delete_what_people_say_url"),
    
    
        
]