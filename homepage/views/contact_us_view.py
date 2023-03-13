from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from decouple import config
from dashboard.models import BUDGET, LetsTalk, Subscribe
from django.conf import settings


class ContactUs(View):

    def get(self, request):
        return render(request, 'contact_us.html', {'BUDGET': BUDGET, 'title': "Contact Us"})

    def post(self, request):
        data = request.POST
        type_ = int(data.get('type'))
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
        budget = data.get('budget')
        phone = data.get('phone')
        if type_ == 2:
            LetsTalk.objects.create(name= name, phone_number= phone, email= email, message= message, budget= int(budget))
            from django.core.mail import EmailMultiAlternatives
            data = ''


            text_content = ""
            html_content = "<p>Name:{}&nbsp;<br>Email:{}&nbsp;<br>Phone Number:{}&nbsp;</p>\
                                            <p>Message:{}</p> \
                                            ".format(name,email, phone, message)

            msg = EmailMultiAlternatives('Lets Talk', text_content, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
            msg.attach_alternative(html_content, "text/html")
            msg.send()



            return JsonResponse({'success': True,})
        else:
            already_existes = Subscribe.objects.filter(email=email).first()
            email_existes = False
            if already_existes:
                email_existes = True
            else:
                Subscribe.objects.create(email= email)
            return JsonResponse({'success': True, 'email_existes': email_existes })
