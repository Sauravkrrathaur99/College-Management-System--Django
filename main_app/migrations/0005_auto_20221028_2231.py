# Generated by Django 3.1.1 on 2022-10-28 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20221028_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavereportstaff',
            name='attachment',
            field=models.FileField(blank=True, default=None, upload_to='attachment/'),
        ),
    ]
