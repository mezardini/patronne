# Generated by Django 4.0.4 on 2024-06-26 11:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('points_balance', models.IntegerField(default=0)),
                ('datetime_added', models.DateTimeField(auto_now_add=True)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patron', to='restaurants.restaurant')),
            ],
        ),
    ]
