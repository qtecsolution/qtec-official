from django.shortcuts import render
from django.views import View

from dashboard.models import WhatProjectHaveWeDone


class IndexView(View):

    def get(self, request):
        project_done = WhatProjectHaveWeDone.objects.values()
        print(project_done,'------------')
        context = {
            'project_done': project_done
        }
        return render(request, 'index.html', context)