# Generated by Django 4.0.4 on 2024-06-26 11:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('datetime_added', models.DateTimeField(auto_now_add=True)),
                ('reward_program_name', models.CharField(max_length=255)),
                ('reward_program_description', models.TextField()),
                ('points_per_dollar', models.FloatField()),
                ('minimum_order_value', models.IntegerField()),
                ('maximum_points_per_order', models.IntegerField()),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patron', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
