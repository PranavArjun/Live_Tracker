# Generated by Django 3.2.3 on 2021-07-14 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_orders'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='truck3',
            new_name='Order',
        ),
        migrations.DeleteModel(
            name='orders',
        ),
        migrations.DeleteModel(
            name='truck1',
        ),
        migrations.DeleteModel(
            name='truck2',
        ),
    ]
