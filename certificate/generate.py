import os
from PIL import Image,ImageDraw,ImageFont
from .models import Certificate
import qrcode


BACKEND_URL="http://127.0.0.1:8000/"
# font_type=ImageFont.truetype("assets/fonts/tapestry.ttf",100) 
def generate_certificate(name,event_name,name_x_pos,name_y_pos,name_box_height,name_box_width,event_x_pos,event_y_pos,event_box_height,event_box_width,font_family):
    
    certificate_template='assets/templates/certificate_template_{}.png'.format(event_name)
    output_dir="assets/certificates/{}".format(event_name)
    font_file="assets/fonts/"+font_family+".ttf"
    if not os.path.exists(output_dir):
        print("Created "+output_dir)
        os.makedirs(output_dir)
    else:
        print(output_dir+" Already Present")
    
    
            
    

    img=Image.open(certificate_template)
    name_box=((name_x_pos,name_y_pos,name_box_width,name_box_height))
    event_box=((event_x_pos,event_y_pos,event_box_width,event_box_height))

    

    draw=ImageDraw.Draw(img)
    draw.multiline_text(xy=(name_box[0],name_box[1]),text=name,fill=(0,0,0),font=compute_font(name_box,name,font_file))
    draw.multiline_text(xy=(event_box[0],event_box[1]),text=event_name,fill=(0,0,0),font=compute_font(event_box,event_name,font_file))
    certificate=Certificate(name=name,event_name=event_name,font_family=font_family,name_x_pos=name_x_pos,name_y_pos=name_y_pos,name_box_height=name_box_height,name_box_width=name_box_width,event_x_pos=event_x_pos,event_y_pos=event_y_pos,event_box_height=event_box_height,event_box_width=event_box_width,file=output_dir+"/{}.png".format(name))
    certificate.save()



    # Qrcode
    qr = qrcode.QRCode(box_size=4)
    qr.add_data(BACKEND_URL+"certificate/verify?id={}".format(certificate.id))
    qr.make()
    img_qr = qr.make_image()
    pos = (img.size[0] - img_qr.size[0], img.size[1] - img_qr.size[1])
    img.paste(img_qr, pos)
    




    img.save(output_dir+"/{}.png".format(name))
    
    print("Generated certificate for {}".format(name))
    return output_dir+"/{}.png".format(name)


def compute_font(box,text,font_file):
    font_size=100
    font=ImageFont.truetype(font_file,font_size)
    size=None
    while (size is None or size[0] > box[2] or size[1] > box[3]) and font_size > 0:
        font = ImageFont.truetype(font_file, font_size)
        size = font.getsize_multiline(text)
        # print("Name Size : ",name_size)
        font_size -= 1
    return font
