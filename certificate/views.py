from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .generate import generate_certificate
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
        name_x_pos=int(request.POST['name_x_pos'])
        name_y_pos=int(request.POST['name_y_pos'])
        event_x_pos=int(request.POST['event_x_pos'])
        event_y_pos=int(request.POST['event_y_pos'])
        font_size=int(request.POST['font_size']) 
    except Exception as e:
        print(e)
        return JsonResponse({'status':400,'message':'not enough data'})


    generate_certificate(name,event_name,name_x_pos,name_y_pos,event_x_pos,event_y_pos,font_size)
    return JsonResponse({'status':200,'message':'Accepted'})
    