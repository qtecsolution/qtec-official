from django.shortcuts import render
from django.views import View


class AlreadyDoneView(View):

    def get(self, request):
        return render(request, 'already_done.html')