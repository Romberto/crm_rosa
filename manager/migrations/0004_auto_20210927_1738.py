# Generated by Django 3.2.7 on 2021-09-27 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_alter_case_tegs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='tegs',
        ),
        migrations.AddField(
            model_name='case',
            name='tegName',
            field=models.CharField(choices=[('1', 'пшеница'), ('2', 'семечка'), ('3', 'майонез'), ('4', 'овес'), ('5', 'жмых'), ('6', 'кусочек сыра')], default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ProductTegs',
        ),
    ]
