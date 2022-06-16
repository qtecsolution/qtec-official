from django.urls import path

from dashboard.views.dashboard import DashboardView

app_name= 'dashboard'

urlpatterns= [
    path('dashboard/', DashboardView.as_view(), name= 'dashboard_url')
]