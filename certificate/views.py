from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .generate import generate_certificate
from django.http import FileResponse
from .models import Certificate
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
        name_box_height=int(request.POST['name_box_height'])
        name_box_width=int(request.POST['name_box_width'])
        event_x_pos=int(request.POST['event_x_pos'])
        event_y_pos=int(request.POST['event_y_pos'])
        event_box_height=int(request.POST['event_box_height'])
        event_box_width=int(request.POST['event_box_width'])

        
        if not os.path.exists("assets/fonts/"+font_family+".ttf"):
            raise Exception("Font Not present")

        if not os.path.exists('assets/templates/certificate_template_{}.png'.format(event_name)):
            raise Exception("Event Certificate Template not Present")
         
    except Exception as e:
        print(e)
        return JsonResponse({'status':400,'message':'not enough data'})


    image_path=generate_certificate(name,event_name,name_x_pos,name_y_pos,name_box_height,name_box_width,event_x_pos,event_y_pos,event_box_height,event_box_width,font_family)  
    
    # This portion returns the path of the file on the server.
    return JsonResponse({'status':200,'message':'Accepted','file':image_path})

    # This portion return the file through http
    image=open(image_path,'rb')
    response=FileResponse(image)
    return response
    

def list_certificates(request):
    certificate_dir="assets/certificates/"
    result={}
    try :
        event=request.GET['event']
        certificates=[]
        for certificate in os.listdir(certificate_dir+event):
            certificates.append(certificate_dir+event+"/"+certificate)
        result[event]=certificates
        return JsonResponse(result)
    
    except Exception as e:
        
        for event in os.listdir(certificate_dir):
            certificates=[]
            for certificate in os.listdir(certificate_dir+event):
                certificates.append(certificate_dir+event+"/"+certificate)
            result[event]=certificates
        # print(result)
        return JsonResponse(result)



def verify(request):
    current_certificate=None
    certificate_id=request.GET.get("id")
    try:
        current_certificate=Certificate.objects.get(id=certificate_id)
    except Exception as e:
        print(e)
    if current_certificate:
        context={
            'verified':True,
            'name':current_certificate.name,
            'event_name':current_certificate.event_name,
        }
        return render(request,'certificate/verify.html',context)
    else:
        return HttpResponse("No certificate found")
