# Generated by Django 4.2.4 on 2023-10-03 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='account_name',
            field=models.CharField(default=10, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registration',
            name='device_details',
            field=models.CharField(default=20, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registration',
            name='user_category',
            field=models.CharField(choices=[('3d', '3D PRINTING'), ('aqua', 'AQUA CULTURE'), ('water', 'WATER BODY MANAGEMENT')], default=None, max_length=20),
        ),
    ]
