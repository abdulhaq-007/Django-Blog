# Generated by Django 3.2.4 on 2022-01-29 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_post_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id']},
        ),
    ]