# Generated by Django 3.2.7 on 2021-10-07 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0025_alter_casemodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='statusmodel',
            name='is_active',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
