# Generated by Django 4.1.4 on 2023-01-02 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0002_task_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(default='Image/None/Noimg.jpg', upload_to='Images/'),
        ),
    ]
