# Generated by Django 3.0.5 on 2020-07-26 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20200726_1355'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Opinion',
            new_name='Review',
        ),
        migrations.AlterModelTable(
            name='review',
            table='reviews',
        ),
    ]