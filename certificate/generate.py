import os
from PIL import Image,ImageDraw,ImageFont

def generate_certificate(name,event_name,name_x_pos,name_y_pos,event_x_pos,event_y_pos,font_size):
    font=ImageFont.truetype('assets/fonts/tapestry.ttf',font_size)
    certificate_template='assets/templates/certificate_template_{}.png'.format(event_name)
    output_dir="assets/certificates/{}".format(event_name)
    name=name
    if not os.path.exists(output_dir):
        print("Created "+output_dir)
        os.makedirs(output_dir)
    else:
        print(output_dir+" Already Present")
    
    
            
            

    img=Image.open(certificate_template)
    draw=ImageDraw.Draw(img)
    draw.text(xy=(name_x_pos,name_y_pos),text=name,fill=(0,0,0),font=font)
    draw.text(xy=(event_x_pos,event_y_pos),text=event_name,fill=(0,0,0),font=font)
    img.save(output_dir+"/{}.png".format(name))
    print("Generated certificate for {}".format(name))
    return output_dir+"/{}.png".format(name)
