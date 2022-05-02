from django.urls import path,include
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('home/',views.home,name="Home"),
    path('add_template',csrf_exempt(views.add_template),name="Add Template"),
]
