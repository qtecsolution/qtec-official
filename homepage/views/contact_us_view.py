from django.shortcuts import render
from django.views import View


class ContactUs(View):

    def get(self, request):
        return render(request, 'contact_us.html')