# Generated by Django 3.2 on 2021-05-10 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_order_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.IntegerField(default=100),
        ),
    ]