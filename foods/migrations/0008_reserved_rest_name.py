# Generated by Django 3.0.6 on 2020-06-21 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0007_auto_20200621_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserved',
            name='rest_name',
            field=models.ForeignKey(default='boof', on_delete=django.db.models.deletion.CASCADE, to='foods.restaurant'),
        ),
    ]
