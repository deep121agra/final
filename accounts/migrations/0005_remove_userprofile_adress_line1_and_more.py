# Generated by Django 5.1.2 on 2024-10-23 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='adress_line1',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='adress_line2',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='adress',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]