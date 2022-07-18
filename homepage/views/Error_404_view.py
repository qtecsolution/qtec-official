
from django.shortcuts import render
from django.views import View


class Error_404(View):
    def get(self, request):
        context = {
            'title': "Error",
        }
        return render(request, 'error_404/error.html',context)

   
