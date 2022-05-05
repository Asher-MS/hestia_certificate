from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .generate import generate_certificate
from django.http import FileResponse
import os
# Create your views here.
def home(request):
    
    return HttpResponse('<h1>This is the home page of certificate generator</h1>')
    
def save_certificate_template(certificate_template,event_name):
    destination=open('assets/templates/certificate_template_{}.png'.format(event_name),'wb+') # open the destination file
    
    for chunk in certificate_template.chunks(): # Save the file
        destination.write(chunk)  



def add_template(request):
    if(request.method=='POST'):
        try:
            certificate_template=request.FILES['certificate_template']
            event_name=request.POST['event_name']
        except Exception as e:
            return JsonResponse({"status":400,"message":"certificate template or event_name not given"})
        save_certificate_template(certificate_template,event_name)
        print("Certificate Saved")
        return JsonResponse({"status":200,"message":"Accepted"})

    else:
        return HttpResponse("<h1>POST only</h1>")

def certificate(request):
    try:
        name=request.POST['name']
        
        event_name=request.POST['event_name']
        font_family=request.POST['font_family']
        name_x_pos=int(request.POST['name_x_pos'])
        name_y_pos=int(request.POST['name_y_pos'])
        event_x_pos=int(request.POST['event_x_pos'])
        event_y_pos=int(request.POST['event_y_pos'])
        
        if not os.path.exists("assets/fonts/"+font_family+".ttf"):
            raise Exception("Font Not present")

        if not os.path.exists('assets/templates/certificate_template_{}.png'.format(event_name)):
            raise Exception("Event Certificate Template not Present")
         
    except Exception as e:
        print(e)
        return JsonResponse({'status':400,'message':'not enough data'})


    image_path=generate_certificate(name,event_name,name_x_pos,name_y_pos,event_x_pos,event_y_pos,font_family)
    
    # This portion returns the path of the file on the server.
    return JsonResponse({'status':200,'message':'Accepted','file':image_path})

    # This portion return the file through http
    image=open(image_path,'rb')
    response=FileResponse(image)
    return response
    

def list_certificates(request):
    result={}
    for event in os.listdir("assets/certificates"):
        certificates=[]
        for certificate in os.listdir("assets/certificates/"+event):
            certificates.append(certificate)
            
        result[event]=certificates
    # print(result)
    return JsonResponse(result)
