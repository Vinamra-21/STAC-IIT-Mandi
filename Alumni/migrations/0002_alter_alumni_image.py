# Generated by Django 5.1 on 2024-10-02 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumni', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumni',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images/Alumni'),
        ),
    ]
