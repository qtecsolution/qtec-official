from django.contrib import admin
from django.apps import apps

from dashboard.models import YouTubeVideo

depot_app_config = apps.get_app_config('dashboard')
for model in depot_app_config.get_models():
        admin.site.register(model)

