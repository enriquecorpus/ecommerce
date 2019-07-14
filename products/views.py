import products.models
import django.http
import json


def index(request):
    category = products.models.Category.objects.get(pk=1)
    context = list(products.models.Product.objects.filter(category_id=category.id).values())
    return django.http.response.JsonResponse(data=context, safe=False)
