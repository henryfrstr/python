from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from store.models import Product


def hello(request):

    # product = get_object_or_404(Product, id=0)
    # product = Product.objects.filter(id=0).exists()
    queryset = Product.objects.filter(unit_price__range=(20, 30))

    return render(request, 'playground/hello.html', {'name': 'Henry', 'product': queryset})
