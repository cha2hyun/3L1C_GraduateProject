# Generated by Django 3.0.3 on 2020-03-03 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='companydb',
            name='hi',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]