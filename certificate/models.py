from django.db import models

# Create your models here.

class Certificate(models.Model):
    name=models.CharField(max_length=1000)
    event_name=models.CharField(max_length=1000)
    font_family=models.CharField(max_length=1000)
    name_x_pos=models.IntegerField(default=0)
    name_y_pos=models.IntegerField(default=0)
    name_box_height=models.IntegerField(default=100)
    name_box_width=models.IntegerField(default=100)
    event_x_pos=models.IntegerField(default=0)
    event_y_pos=models.IntegerField(default=0)
    event_box_height=models.IntegerField(default=100)
    event_box_width=models.IntegerField(default=100)
    file=models.CharField(max_length=1000)
    def __str__(self):
        return self.name+"-"+self.event_name
    
