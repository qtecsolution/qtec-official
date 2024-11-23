from django.shortcuts import render
from django.views import View

from dashboard.models import HomeClients, OurGallery, TeamMembers, WhatPeopleSay, WhatProjectHaveWeDone, Blog, YouTubeVideo


class IndexView(View):

    def get(self, request):
        project_done_all = WhatProjectHaveWeDone.objects.filter(display=True, homepage= True).order_by("priority").all()

        web_project = project_done_all.filter(project_type__icontains='1')
        app_project = project_done_all.filter(project_type__icontains='2')

        ui_ux = project_done_all.filter(project_type__icontains='3')

        blog = Blog.objects.filter(display=True).order_by('-id')
        blog = blog[:4] if blog.count() > 4 else blog
        home_clients = HomeClients.objects.first()
        what_people_say = WhatPeopleSay.objects.values()
        members = TeamMembers.objects.order_by('priority').values()
        our_gallery = OurGallery.objects.all().order_by("priority")
        video_link = YouTubeVideo.objects.filter(page=YouTubeVideo.HOME).first()
        context = {
            'project_done_exists': project_done_all.exists(),
            'title': "Home",
            'project_done': project_done_all,
            'web_project': web_project,
            'app_project': app_project,
            'ui_ux': ui_ux,
            'blogs': blog,
            'home_clients': home_clients,
            'what_people_say': what_people_say,
            'members': members,
            'our_gallery': our_gallery,
            'video_link': video_link,
        }

        return render(request, 'index.html', context)


class CaseStudyView(View):

    def get(self, request):
        project_done_all = WhatProjectHaveWeDone.objects.filter(display=True).order_by("priority").all()

        web_project = project_done_all.filter(project_type__icontains='1')
        app_project = project_done_all.filter(project_type__icontains='2')

        ui_ux = project_done_all.filter(project_type__icontains='3')

        context = {
            'project_done_exists': project_done_all.exists(),
            'title': "Case Study",
            'project_done': project_done_all,
            'web_project': web_project,
            'app_project': app_project,
            'ui_ux': ui_ux,

        }
        return render(request, 'case_study_list.html', context)
