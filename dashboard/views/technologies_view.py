from django.shortcuts import redirect, render
from django.views import View

from dashboard.models import Technologies, TechnologyFeatures
from django.contrib import messages



class TechnologiesView(View):
    def get(self, request):
        technologies = Technologies.objects.all()
        technology_features = TechnologyFeatures.objects.values('id','title')
        print("technology_features::::", technology_features)
        context = {
            "technologies" : technologies,
            "technology_features" : technology_features
        }
        return render(request, 'technologies.html', context)
        
    def post(self, request):
        data = request.POST
        file = request.FILES
        if request.resolver_match.url_name == "save_technologies_url":
            title = data.get('title')
            description = data.get('description')
            image = file.get('image')

            if not title or not description or not image:
                messages.error(request, 'Invalid input!')
            else:
                technologies = Technologies()
                technologies.title = title
                technologies.description = description
                technologies.image = image
                technologies.save()
                messages.success(request, 'Data save successful!')

            return redirect('dashboard:technologies_url')

        if request.resolver_match.url_name == "delete_technologies_url":
            request_id = data.get('id')
            technologies = Technologies.objects.filter(id=request_id).first().delete()
            messages.success(request, 'Delete successful')
            return redirect('dashboard:technologies_url')
        
