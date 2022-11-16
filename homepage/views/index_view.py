from django.shortcuts import render
from django.views import View

from dashboard.models import HomeClients, WhatPeopleSay, WhatProjectHaveWeDone, Blog


class IndexView(View):

    def get(self, request):
        project_done_all = WhatProjectHaveWeDone.objects.all()
   
        web_project = project_done_all.filter(project_type__icontains = '1')
        app_project = project_done_all.filter(project_type__icontains = '2')
        
        ui_ux = project_done_all.filter(project_type__icontains = '3')

        blog = Blog.objects.order_by('-id')
        blog = blog[:4] if blog.count() > 4 else blog
        home_clients = HomeClients.objects.first()
        what_people_say = WhatPeopleSay.objects.values()
        context = {
            'project_done_exists': project_done_all.exists(),
            'title': "Home",
            'project_done': project_done_all,
            'web_project': web_project,
            'app_project': app_project,
            'ui_ux':ui_ux,
            'blogs': blog,
            'home_clients': home_clients,
            'what_people_say': what_people_say
        }

        return render(request, 'index.html', context)

