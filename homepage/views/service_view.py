from django.shortcuts import render
from django.views import View

from dashboard.models import ServiceDetailsProject


class ServiceView(View):

    def get(self, request):
        return render(request, 'service/service.html', {'title': "Service"})


class ServiceDetailsView(View):

    def get(self, request, slug):
        projects = ServiceDetailsProject.objects.filter(slug=slug)

        if slug == 'software-solutions-development':
            return render(request, 'service/software_solution_development.html', {'title': "Service Details", "projects": projects})
