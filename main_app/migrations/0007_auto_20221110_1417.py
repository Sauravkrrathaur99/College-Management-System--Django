# Generated by Django 3.1.1 on 2022-11-10 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_leavereportstudent_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
