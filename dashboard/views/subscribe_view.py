from django.shortcuts import render
from django.views import View

from dashboard.models import Subscribe


class SubscribeView(View):
    def get(self, request):
        subscribers = Subscribe.objects.values('id','email')
        context = {
            "subscribers" : subscribers,
        }
        return render(request, 'subscribe.html', context)