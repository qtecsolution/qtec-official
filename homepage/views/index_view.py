from django.shortcuts import render
from django.views import View

from dashboard.models import WhatProjectHaveWeDone, Blog


class IndexView(View):

    def get(self, request):
        project_done_all = WhatProjectHaveWeDone.objects.all()
        project_done = project_done_all.values()
        web_project = project_done.filter(project_type = 1)
        app_project = project_done.filter(project_type = 2)
        ui_ux = project_done.filter(project_type = 3)


        blog = Blog.objects.order_by('-id')
        blog = blog[:4] if blog.count() > 4 else blog
        context = {
            'project_done_exists': project_done_all.exists(),
            'title': "Homepage",
            'project_done': project_done,
            'web_project': web_project,
            'app_project': app_project,
            'ui_ux':ui_ux,
            'blogs': blog
        }

        return render(request, 'index.html', context)

