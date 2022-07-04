from django.shortcuts import render
from django.views import View

from dashboard.models import Technologies
from django.contrib import messages



class TechnologiesView(View):
    def get(self, request):
        technologies = Technologies.objects.order_by("-id").values()
        context = {
            "technologies" : technologies,
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

            return self.get(request)
        if request.resolver_match.url_name == "delet_technologies_url":
            request_id = data.get('id')
            technologies = Technologies.objects.filter(id=request_id).first().delete()
            messages.success(request, 'Delete successful')
            return self.get(request)
        
