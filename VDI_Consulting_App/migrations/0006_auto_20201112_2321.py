# Generated by Django 2.2 on 2020-11-13 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VDI_Consulting_App', '0005_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_product', to='VDI_Consulting_App.Product'),
        ),
    ]
