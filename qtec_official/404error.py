
from django.shortcuts import render
from django.template import RequestContext


def handler404(request, *args, **argv):
    return render(request, '404error.html',{'title':'Error'})


def handler500(request, *args, **argv):
    return render(request, 'homepage/404error.html', {'title':'Error'})

