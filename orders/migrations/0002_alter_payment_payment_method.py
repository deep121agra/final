# Generated by Django 5.1.2 on 2024-11-09 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('RazorPay', 'RazorPay')], max_length=100),
        ),
    ]
