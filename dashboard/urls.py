from django.urls import path
from dashboard.views.already_done_view import AlreadyDoneView

from dashboard.views.dashboard import DashboardView
from dashboard.views.subscribe_view import SubscribeView

app_name= 'dashboard'

urlpatterns= [
    path('dashboard/', DashboardView.as_view(), name= 'dashboard_url'),
    path('already-done/', AlreadyDoneView.as_view(), name= 'already_done_url'),
    path('subscribe/', SubscribeView.as_view(), name= 'subscribe_url'),
    
]