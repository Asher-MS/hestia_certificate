from django.urls import path,include
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('home/',views.home,name="Home"),
    path('add_template',csrf_exempt(views.add_template),name="Add Template"),
    path('generate_certificate',csrf_exempt(views.certificate),name="Generate Certificate"),
    path('list_certificates',csrf_exempt(views.list_certificates),name="List Certificates"),
    path('verify',csrf_exempt(views.verify),name="verify-certificate")

]
