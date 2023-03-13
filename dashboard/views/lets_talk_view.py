from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View

from dashboard.models import BUDGET, LETS_TAlK_STATUS, LetsTalk
from django.contrib import messages



class LetsTalkView(View):

    def get(self, request):
        lets_talk = LetsTalk.objects.all().order_by('-id')
        context = {
            "lets_talk" : lets_talk,
            "status" :LETS_TAlK_STATUS,
            "budget" : BUDGET,
        }
        return render(request, 'lets_talk.html', context)

    def post(self, request):
        if request.resolver_match.url_name == "delete_lets_talk_url":
            request_id = request.POST.get('id')
            lets_talk = LetsTalk.objects.filter(id=request_id).first().delete()
            messages.success(request, 'Data deleted successful!')
            return redirect('dashboard:lets_talk_url')

        if request.resolver_match.url_name == "lets_talk_status_change_url":
            request_id = request.POST.get('id') 
            lets_talk = LetsTalk.objects.filter(id=request_id).first()
            lets_talk.status = request.POST.get('status')
            lets_talk.save()
            return JsonResponse({})