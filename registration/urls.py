import django.conf.urls
from django.urls import path
import registration.views
import django.views.generic

urlpatterns = [
    path('', registration.views.index, name='index'),
    path('signup/', registration.views.signup, name='signup'),
]
