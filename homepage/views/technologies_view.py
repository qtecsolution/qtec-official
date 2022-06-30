from django.shortcuts import render
from django.views import View

from dashboard.models import Technologies


class TechnologiesView(View):

    def get(self, request, slug):
        technologies = Technologies.objects.filter(slug=slug)
        print("technologies:::::::", technologies)
        return render(request, 'technology/technologies.html')

        # if slug == 'software-solutions-development':
        #     return render(request, 'service/software_solution_development.html', {'title': "Service Details", "projects": projects})
      