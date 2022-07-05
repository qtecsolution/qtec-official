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
        if slug == 'ui-ux-design':
            return render(request, 'service/ui_ux_design.html', {'title': "UI UX Design", "projects": projects})
        if slug == 'ecommerce-solutions':
            return render(request, 'service/e_commerce_solutions.html', {'title': "E Commerce Solutions", "projects": projects})
        if slug == 'mobile-application-development':
            return render(request, 'service/mobile_application_development.html', {'title': "Mobile Application Development", "projects": projects})
        if slug == 'lms-solutions':
            return render(request, 'service/lms_solutions.html', {'title': "LMS Solutions", "projects": projects})
        if slug == 'logistics-solutions':
            return render(request, 'service/logistics_solutions.html', {'title': "Logistics Solutions", "projects": projects})
															
														
