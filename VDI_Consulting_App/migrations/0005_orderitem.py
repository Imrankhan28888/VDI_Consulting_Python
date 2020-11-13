# Generated by Django 2.2 on 2020-11-13 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VDI_Consulting_App', '0004_auto_20201111_0024'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('item_cost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('Cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='VDI_Consulting_App.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_product', to='VDI_Consulting_App.cart')),
            ],
        ),
    ]