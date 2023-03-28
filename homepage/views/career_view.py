from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.core.mail import EmailMessage
import os
from dashboard.models import CurrentOpportunities, ApplyForThisPosition


class CareerView(View):

    def get(self, request):
        careers = CurrentOpportunities.objects.filter(display=True).all().order_by("-deadline")
        is_careers = CurrentOpportunities.objects.exists()
        context = {
            'title': "Career",
            'careers': careers,
            'is_careers' : is_careers
        }
        return render(request, 'career/career_page.html', context)


def send_career_email_to_qtec(subject, file_contents, first_name, last_name, email):
    subject = subject
    body ="First Name: {} , Last Name: {}, Email: {}".format(first_name, last_name, email)
    from_email = 'contact.qtec@gmail.com'
    to_email = ['qtec.careers@gmail.com']

    email = EmailMessage(subject, body, from_email, to_email)

    email.attach('{} cv for position {}'.format(first_name, subject), file_contents, 'application/pdf')
    email.send()


class CareerDetailsView(View):

    def get(self, request, slug= None):
        career = CurrentOpportunities.objects.get(slug = slug,display=True)

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
        
        career = CurrentOpportunities.objects.get(id = career_id)

        apply_ = ApplyForThisPosition.objects.create(current_opportunities_id= career_id ,first_name= firstname, last_name= lastname, email= careeremail, upload_cv= image)
        title = career.title
        file_contents = apply_.upload_cv.read()
        send_career_email_to_qtec(title, file_contents, firstname, lastname, careeremail)
        
        return JsonResponse({})