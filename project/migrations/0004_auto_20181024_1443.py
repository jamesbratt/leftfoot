# Generated by Django 2.1.2 on 2018-10-24 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20181024_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='scope',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='state',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
