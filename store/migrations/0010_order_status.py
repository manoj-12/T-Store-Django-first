# Generated by Django 3.2.7 on 2021-10-09 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
