from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from dashboard.models import CurrentOpportunities, ApplyForThisPosition


class CareerView(View):

    def get(self, request):
        careers = CurrentOpportunities.objects.all()
        is_careers = CurrentOpportunities.objects.exists()
        context = {
            'title': "CAREER",
            'careers': careers,
            'is_careers' : is_careers
        }
        return render(request, 'career/career_page.html', context)


class CareerDetailsView(View):

    def get(self, request, slug= None):
        career = CurrentOpportunities.objects.get(slug = slug)

        context = {
            'title': "Career Details of {}".format(career.title),
            'career': career
        }
        return render(request, 'career/career_details.html', context)

    def post(self, request, slug= None):
        data = request.POST
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        careeremail = data.get('careeremail')
        image = request.FILES.get('image')
        career_id= data.get('career_id')
        ApplyForThisPosition.objects.create(current_opportunities_id= career_id ,first_name= firstname, last_name= lastname, email= careeremail, upload_cv= image)
        return JsonResponse({})