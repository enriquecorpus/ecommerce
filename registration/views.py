import registration.forms
import registration.models
import django.template.response
import django.http
import django.urls

_GET = 'GET'
_POST = 'POST'


def index(request):
    return django.http.JsonResponse(data={'data': 'success'})


def signup(request):
    context = {}
    if request.method == _GET:
        context['form'] = registration.forms.InitRegistrationForm()
    elif request.method == _POST:
        context['form'] = registration.forms.InitRegistrationForm(request.POST)
        if context['form'].is_valid():
            form_data = context['form'].cleaned_data
            user = registration.models.User()
            user.email = form_data.get('email')
            user.first_name = form_data.get('first_name')
            user.middle_name = form_data.get('middle_name')
            user.last_name = form_data.get('last_name')
            user.save()
            # return django.http.HttpResponseRedirect(django.urls.reverse('registration:verify'))
            return django.http.JsonResponse(data={'data': 'success'})
    return django.template.response.TemplateResponse(request, 'registration/signup.html', context=context)
