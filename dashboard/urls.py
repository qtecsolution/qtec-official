from django.urls import path
from dashboard.views.already_done_view import AlreadyDoneView, CaseStudyEditView

from dashboard.views.dashboard import DashboardView
from dashboard.views.subscribe_view import SubscribeView
from dashboard.views.technologies_view import TechnologiesView

app_name= 'dashboard'

urlpatterns= [
    path('dashboard/', DashboardView.as_view(), name= 'dashboard_url'),

    path('already-done/', AlreadyDoneView.as_view(), name= 'already_done_url'),
    path('already-done-delete/', AlreadyDoneView.as_view(), name= 'delet_what_done_url'),
    path('already-done-edit/', AlreadyDoneView.as_view(), name= 'edit_what_project_done_url'),
    path('already-done-save/', AlreadyDoneView.as_view(), name= 'save_what_done_url'),
    path('case-study-edit/<int:id>/', CaseStudyEditView.as_view(), name= 'case_study_edit_url'),

    path('subscribe/', SubscribeView.as_view(), name= 'subscribe_url'),

    path('technologies/', TechnologiesView.as_view(), name= 'technologies_url'),
    path('technologies-save/', TechnologiesView.as_view(), name= 'save_technologies_url'),
    path('technologies-delete/', TechnologiesView.as_view(), name= 'delet_technologies_url'),    
]