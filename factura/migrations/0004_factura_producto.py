# Generated by Django 4.2.2 on 2023-06-20 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0003_producto_factura_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='factura.producto'),
        ),
    ]
