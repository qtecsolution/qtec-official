from django.shortcuts import redirect, render
from django.views import View

from dashboard.models import Technologies, TechnologyFeatures
from django.contrib import messages



class TechnologiesView(View):
    def get(self, request):
        if request.resolver_match.url_name == "save_technologies_url":
            technology_features = TechnologyFeatures.objects.all()
            context = {
                "technology_features" : technology_features,
            }
            return render(request, 'partial/technologies_create.html', context)
        else:
            technologies = Technologies.objects.all()
            technology_features = TechnologyFeatures.objects.all()
            context = {
                "technologies" : technologies,
                "technology_features" : technology_features
            }
            return render(request, 'technologies.html', context)
        
    def post(self, request):
        data = request.POST
        file = request.FILES
        if request.resolver_match.url_name == "save_technologies_url":
            technologies = Technologies()
            technologies.title = data.get('title')
            technologies.description = data.get('description')
            technologies.image = file.get('image')
            technologies.technology_details_title = data.get('technology_details_title')
            technologies.technology_detail_description = data.get('technology_detail_description')
            technologies.technology_detail_thumbnail = file.get('technology_detail_thumbnail')
            technologies.why_this_technologies_title = data.get('why_this_technologies_title')
            technologies.why_this_technologies_description = data.get('why_this_technologies_description')
            technologies.why_this_technologies_image = file.get('why_this_technologies_image')
            technologies.why_choice_title = data.get('why_choice_title')
            technologies.why_choice_description = data.get('why_choice_description')
            technologies.why_choice_image = file.get('why_choice_image')
            technologies.save()
            technology_features = data.getlist('technology_features')
            technologies.technology_features.add(*technology_features)
            messages.success(request, 'Data save successful!')

            return redirect('dashboard:technologies_url')

        if request.resolver_match.url_name == "delete_technologies_url":
            request_id = data.get('id')
            technologies = Technologies.objects.filter(id=request_id).first().delete()
            messages.success(request, 'Delete successful')
            return redirect('dashboard:technologies_url')
        
