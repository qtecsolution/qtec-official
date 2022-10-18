from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from dashboard.models import SUBSCRIBE_STATUS, Subscribe


class SubscribeView(View):
    def get(self, request):
        subscribers = Subscribe.objects.values().order_by('-id')
        context = {
            "subscribers" : subscribers,
            "status": SUBSCRIBE_STATUS
        }
        return render(request, 'subscribe.html', context)

    def post(self, request):
        obj = Subscribe.objects.get(id=request.POST.get('id'))
        obj.status = request.POST.get('status')
        # print("request.POST.get('status'):::::::::::", request.POST.get('status'))
        obj.save()
        return JsonResponse({})