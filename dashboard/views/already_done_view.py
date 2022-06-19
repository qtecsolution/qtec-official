from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from dashboard.models import WhatProjectHaveWeDone


class AlreadyDoneView(View):

    def get(self, request):
        what_Done = WhatProjectHaveWeDone.objects.values()
        context = {
            "what_Done" : what_Done,
        }
        return render(request, 'already_done.html', context)
    def post(self, request):
        if request.resolver_match.url_name == "delet_what_done_url":
            request_id = request.POST.get('id')
            what_Done = WhatProjectHaveWeDone.objects.filter(id=request_id).delete()
            return self.get(request)

        if request.resolver_match.url_name == "save_what_done_url":
            pass

            

        