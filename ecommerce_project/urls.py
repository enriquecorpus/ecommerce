"""ecommerce_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.registration, name='registration')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='registration')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django.contrib.admin
import django.views.generic
from django.urls import include
from django.urls import path

urlpatterns = [
    path('JsKahs8hsdnaKlashjhs6/admin/', django.contrib.admin.site.urls),
    path('', django.views.generic.TemplateView.as_view(template_name='ecommerce/index.html'),
         name='home'),
    path('registration/', include(('registration.urls', 'registration'), namespace='registration')),
]

