# Generated by Django 5.1 on 2024-10-02 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alumni', '0002_alter_alumni_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumni',
            name='description',
        ),
        migrations.RemoveField(
            model_name='alumni',
            name='insta',
        ),
        migrations.RemoveField(
            model_name='alumni',
            name='linkedin',
        ),
        migrations.AddField(
            model_name='alumni',
            name='email',
            field=models.EmailField(default='email', max_length=100),
        ),
        migrations.AddField(
            model_name='alumni',
            name='instagram_url',
            field=models.CharField(default='instagram', max_length=100),
        ),
        migrations.AddField(
            model_name='alumni',
            name='linkedin_url',
            field=models.CharField(default='linkedin', max_length=100),
        ),
        migrations.AddField(
            model_name='alumni',
            name='message',
            field=models.CharField(default='andhera_kayam_rahe', max_length=100),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='image',
            field=models.ImageField(default='default.webp', upload_to='images/CoreTeam'),
        ),
        migrations.AlterField(
            model_name='alumni',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
