# Generated by Django 3.2.7 on 2021-09-14 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0002_alter_custom_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom',
            name='number',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
    ]
