# Generated by Django 3.2.3 on 2021-05-26 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_truck1_orderid'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='truck1',
            new_name='Order',
        ),
    ]
