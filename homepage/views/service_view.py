from multiprocessing import context
from django.shortcuts import render
from django.views import View

from dashboard.models import ServiceDetailsProject, WhatProjectHaveWeDone
from django.db.models import Q

class ServiceView(View):

    def get(self, request):
        return render(request, 'service/service.html', {'title': "Service"})


class ServiceDetailsView(View):

    def get(self, request, slug):
        projects = ServiceDetailsProject.objects.filter(slug=slug)

        if slug == 'software-solutions-development':
            projects_done = WhatProjectHaveWeDone.objects.filter(Q(name='Wear Soha') | Q(name='Brightskills') | Q(name='Stech')).all()
            context = {
                'title': "Service Details",
                "projects": projects,
                'projects_done' : projects_done,
            }
            return render(request, 'service/software_solution_development.html', context)
        if slug == 'ui-ux-design':
            projects_done = WhatProjectHaveWeDone.objects.filter(Q(name='Stech') | Q(name='Wear Soha') | Q(name='Supplyline')).all()
            context = {
                'title': "UI UX Design",
                "projects": projects,
                'projects_done' : projects_done,
            }
            return render(request, 'service/ui_ux_design.html', context)
        if slug == 'ecommerce-solutions':
            projects_done = WhatProjectHaveWeDone.objects.filter(Q(name='Odommo Prokash') | Q(name='Decoris Diamonds') | Q(name='Wear Soha')).all()
            context = {
                'title': "E Commerce Solutions",
                "projects": projects,
                'projects_done' : projects_done,
            }
            return render(request, 'service/e_commerce_solutions.html', context)
        if slug == 'mobile-application-development':
            projects_done = WhatProjectHaveWeDone.objects.filter(Q(name='Wear Soha') | Q(name='Brightskills') | Q(name='Supplyline')).all()
            context = {
                'title': "Mobile Application Development",
                "projects": projects,
                'projects_done' : projects_done,
            }
            return render(request, 'service/mobile_application_development.html', context)
        if slug == 'lms-solutions':
            projects_done = WhatProjectHaveWeDone.objects.filter(Q(name='Brightskills') | Q(name='Odommo Prokash ') | Q(name='Lex Intell')).all()
            context = {
                'title': "LMS Solutions",
                "projects": projects,
                'projects_done' : projects_done,
            }
            return render(request, 'service/lms_solutions.html', context)
        if slug == 'Logistics Solutions':
            projects_done = WhatProjectHaveWeDone.objects.filter(Q(name='Odommo Prokash ') | Q(name='Brightskills') | Q(name='Aion Tribute')).all()
            context = {
                'title': "Logistic Solutions",
                "projects": projects,
                'projects_done' : projects_done,
            }
            return render(request, 'service/logistics_solutions.html', context)
															
														
