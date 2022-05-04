import os
from PIL import Image,ImageDraw,ImageFont


# font_type=ImageFont.truetype("assets/fonts/tapestry.ttf",100) 
def generate_certificate(name,event_name,name_x_pos,name_y_pos,event_x_pos,event_y_pos,font_family):
    
    certificate_template='assets/templates/certificate_template_{}.png'.format(event_name)
    output_dir="assets/certificates/{}".format(event_name)
    font_file="assets/fonts/"+font_family+".ttf"
    if not os.path.exists(output_dir):
        print("Created "+output_dir)
        os.makedirs(output_dir)
    else:
        print(output_dir+" Already Present")
    
    
            
    

    img=Image.open(certificate_template)
    name_box=((name_x_pos,name_y_pos,img.size[0]/2,img.size[1]/50))
    event_box=((event_x_pos,event_y_pos,img.size[0]/2,img.size[1]/50))

    # print("Name Box : ",name_box)
    # print("Event Box : ",event_box)

    # name_font_size=100
    # name_font=ImageFont.truetype("assets/fonts/tapestry.ttf",name_font_size)
    # name_size=None
    # while (name_size is None or name_size[0] > name_box[2] or name_size[1] > name_box[3]) and name_font_size > 0:
    #     name_font = ImageFont.truetype("assets/fonts/tapestry.ttf", name_font_size)
    #     name_size = name_font.getsize_multiline(name)
    #     print("Name Size : ",name_size)
    #     name_font_size -= 1
    # print("Name Font:",name_font_size)



    # event_font_size=100
    # event_font=ImageFont.truetype("assets/fonts/tapestry.ttf",event_font_size)
    # event_size=None
    # while (event_size is None or event_size[0] > event_box[2] or event_size[1] > event_box[3]) and event_font_size > 0:
    #     event_font = ImageFont.truetype("assets/fonts/tapestry.ttf", event_font_size)
    #     event_size = event_font.getsize_multiline(event_name)
    #     event_font_size -= 1
    # print("Event Font:",event_font_size)

    draw=ImageDraw.Draw(img)
    draw.multiline_text(xy=(name_box[0],name_box[1]),text=name,fill=(0,0,0),font=compute_font(name_box,name,font_file))
    draw.multiline_text(xy=(event_box[0],event_box[1]),text=event_name,fill=(0,0,0),font=compute_font(event_box,event_name,font_file))
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
