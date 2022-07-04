from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from dashboard.models import BUDGET, LetsTalk, Subscribe


class ContactUs(View):

    def get(self, request):
        return render(request, 'contact_us.html', {'BUDGET': BUDGET, 'title': "Contact"})

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
        
            return JsonResponse({'success': True,})
        else:
            already_existes = Subscribe.objects.filter(email=email).first()
            email_existes = False
            if already_existes:
                email_existes = True
            else:
                Subscribe.objects.create(email= email)
            return JsonResponse({'success': True, 'email_existes': email_existes })
