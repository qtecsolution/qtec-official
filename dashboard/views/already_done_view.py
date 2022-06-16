from django.shortcuts import render
from django.views import View

from dashboard.models import WhatProjectHaveWeDone


class AlreadyDoneView(View):

    def get(self, request):
        what_Done = WhatProjectHaveWeDone.objects.values()
        context = {
            "what_Done" : what_Done,
        }
        return render(request, 'already_done.html')