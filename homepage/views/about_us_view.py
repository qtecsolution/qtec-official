from django.shortcuts import render
from django.views import View


class AboutUsView(View):

    def get(self, request):

        return render(request, 'about_us.html', {'title': "About Us"})