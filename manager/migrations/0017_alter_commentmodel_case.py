# Generated by Django 3.2.7 on 2021-09-29 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0016_commentmodel_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='case',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='manager.casemodel'),
        ),
    ]
