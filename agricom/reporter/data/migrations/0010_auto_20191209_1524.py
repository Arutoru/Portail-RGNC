# Generated by Django 2.2.5 on 2019-12-09 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0009_auto_20191206_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borne',
            name='picture',
            field=models.ImageField(default='C:\\Users\\Arthur Tankwa\\Documents\\tutos\\programmation\\python\\Django\\Geodjango\\agricom\\defaut.jpg', upload_to=''),
        ),
    ]
