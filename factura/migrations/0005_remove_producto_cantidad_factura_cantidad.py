# Generated by Django 4.2.2 on 2023-06-23 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0004_factura_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='cantidad',
        ),
        migrations.AddField(
            model_name='factura',
            name='cantidad',
            field=models.IntegerField(null=True),
        ),
    ]
