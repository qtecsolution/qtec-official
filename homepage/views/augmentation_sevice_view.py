from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.http import JsonResponse
from dashboard.models import AugmantationBudget, AugmentationService, Service
from django.views.decorators.csrf import csrf_exempt

def augmentation_service(request):
    services = Service.objects.all()
    budgets = AugmantationBudget.objects.all()
    title = "STAFF AUGMENTATION"
    return render(request, 'staff_augmentation.html', {'services': services, 'budgets': budgets, 'title': title})

def augmentation_service_create(request):
    if request.method == "POST":
        name = request.POST['name']
        company = request.POST['company']
        phone = request.POST['phone']
        email = request.POST['email']
        service_id = request.POST['service']
        budget_id = request.POST['budget']
        description = request.POST['description']
        aug_serve = AugmentationService(name=name, company=company, phone=phone, email=email, services=Service.objects.get(pk=service_id), budget=AugmantationBudget.objects.get(pk=budget_id), description=description)
        aug_serve.save()
        message ="Thank You"+ " " + name
        return JsonResponse({'message': message})

def custom_404(request):
    return render(request, 'homepage/404error.html', {'title':'Error'})