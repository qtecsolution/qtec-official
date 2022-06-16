from django.urls import path

from homepage.views.index_view import IndexView

app_name= 'homepage'

urlpatterns= [
    path('', IndexView.as_view(), name="index_url")
]