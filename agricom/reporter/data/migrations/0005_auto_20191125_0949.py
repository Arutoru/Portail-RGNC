# Generated by Django 2.2.5 on 2019-11-25 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0004_incidence_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidence',
            name='picture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
