# Generated by Django 5.1 on 2024-10-01 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoreTeam', '0004_remove_memberdetail_image_url_memberdetail_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberdetail',
            name='position',
            field=models.CharField(default='C', max_length=100),
            preserve_default=False,
        ),
    ]