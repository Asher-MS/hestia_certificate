from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .generate import generate_certificate
# Create your views here.
def home(request):
    
    return HttpResponse('<h1>This is the home page of certificate generator</h1>')
    
def save_certificate_template(certificate_template,template_no):
    destination=open('assets/templates/certificate_template_{}.jpg'.format(template_no),'wb+') # open the destination file
    
    for chunk in certificate_template.chunks(): # Save the file
        destination.write(chunk)  



def add_template(request):
    if(request.method=='POST'):
        try:
            certificate_template=request.FILES['certificate_template']
            template_no=request.POST['template_no']
        except Exception as e:
            return JsonResponse({"status":400,"message":"certificate template or template_no not given"})
        save_certificate_template(certificate_template,template_no)
        print("Certificate Saved")
        return JsonResponse({"status":200,"message":"Accepted"})


    else:
        return HttpResponse("<h1>POST only</h1>")