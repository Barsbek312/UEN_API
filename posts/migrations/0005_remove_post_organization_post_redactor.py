# Generated by Django 4.2.4 on 2024-06-08 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_organization_logo'),
        ('posts', '0004_postimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='organization',
        ),
        migrations.AddField(
            model_name='post',
            name='redactor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='user.redactor'),
        ),
    ]
