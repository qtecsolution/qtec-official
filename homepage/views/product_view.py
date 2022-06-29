from django.shortcuts import render
from django.views import View


class ProductsView(View):

    def get(self, request):
        return render(request, 'product.html', {'title': "PRODUCTS"})