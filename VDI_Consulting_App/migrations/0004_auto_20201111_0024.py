# Generated by Django 2.2 on 2020-11-11 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VDI_Consulting_App', '0003_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]