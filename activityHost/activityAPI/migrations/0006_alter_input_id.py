# Generated by Django 4.0.4 on 2022-05-05 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activityAPI', '0005_alter_master_compdate_alter_master_duedate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]