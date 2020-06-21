# Generated by Django 3.0.6 on 2020-06-21 19:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foods', '0003_admin_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food_date',
            name='had_eaten',
        ),
        migrations.CreateModel(
            name='reserved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reserved_time', models.DateField()),
                ('deliverd', models.BooleanField(default=False)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foods.food_date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
