# Generated by Django 3.1.10 on 2022-05-25 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='file',
            field=models.ImageField(default='certificate.jpg', upload_to='certificates/<django.db.models.fields.CharField>'),
        ),
    ]
