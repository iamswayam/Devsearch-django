# Generated by Django 3.1 on 2021-07-31 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20210726_0157'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='defaut.jpg', null=True, upload_to=''),
        ),
    ]