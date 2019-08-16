import django.views.decorators.http
import products.models
import django.http
import products.models
import django.urls
import django.contrib.auth.decorators
import functools


def _ajax_required(func):
    @functools.wraps(func)
    def _wrapped_view(request, *args, **kwargs):
        if request.is_ajax():
            return func(request, *args, **kwargs)
        return django.core.exceptions.PermissionDenied()

    return _wrapped_view


def index(request):
    category = products.models.Category.objects.get(pk=1)
    context = list(products.models.Product.objects.filter(category_id=category.id).values())
    return django.http.response.JsonResponse(data=context, safe=False)


@django.views.decorators.http.require_POST
def products_search(request):
    if request.POST.get('search_string'):
        search_data = products.models.Search()
        search_data.text = request.POST.get('search_string')
        search_data.save()
    return django.http.HttpResponseRedirect(django.urls.reverse('home'))


class Actions:
    ADD = 'add'
    UPDATE = 'update'
    DELETE = 'delete'

    def __init__(self, request):
        self.request = request

    def add(self):
        _product = products.models.Product()
        _product.title = self.request.POST.get('title')
        _product.category.id = self.request.POST.get('category_id')
        _product.description = self.request.POST.get('description')
        _product.save()

    def update(self):
        pass

    def delete(self):
        pass


class ProductsForm(django.forms.ModelForm):
    class Meta:
        model = products.models.Product
        fields = '__all__'
        # widgets = {'added_by': django.forms.HiddenInput()}


@_ajax_required
@django.views.decorators.http.require_POST
def product_action(request):
    request_action = request.POST.get('action')
    action_ = Actions(request)
    if request_action == Actions.ADD:
        action_.add()
    elif request_action == Actions.UPDATE:
        action_.update()
    elif request_action == Actions.DELETE:
        action_.delete()


def product(request):
    if request.method == 'GET':
        initial_form_data = {}
        return django.shortcuts.render(request, 'products/index.html',
                                       context={'form': ProductsForm(initial=initial_form_data)})
    if request.method == "POST":
        pass
