# Generated by Django 4.0.5 on 2022-06-09 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_seed'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['created']},
        ),
    ]
