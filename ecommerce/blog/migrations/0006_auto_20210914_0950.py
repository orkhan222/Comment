# Generated by Django 3.2.7 on 2021-09-14 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210912_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commet',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
