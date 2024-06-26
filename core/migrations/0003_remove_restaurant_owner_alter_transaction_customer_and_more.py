# Generated by Django 4.0.4 on 2024-06-26 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patrons', '0001_initial'),
        ('restaurants', '0001_initial'),
        ('core', '0002_restaurant_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='owner',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transaction_patron', to='patrons.customer'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_restaurant', to='restaurants.restaurant'),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Restaurant',
        ),
    ]
