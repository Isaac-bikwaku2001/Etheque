# Generated by Django 3.2.8 on 2021-10-17 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etheque', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livre',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]