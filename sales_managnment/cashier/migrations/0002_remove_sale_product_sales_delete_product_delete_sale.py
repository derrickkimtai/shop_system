# Generated by Django 5.0.6 on 2024-07-02 13:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashier', '0001_initial'),
        ('manager', '0002_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='product',
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_sold', models.PositiveIntegerField()),
                ('sale_price', models.FloatField()),
                ('payment_method', models.CharField(choices=[('Cash', 'Cash'), ('Mpesa', 'Mpesa')], max_length=100)),
                ('mpesa_code', models.CharField(blank=True, max_length=100, null=True)),
                ('stock_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.stock')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Sale',
        ),
    ]
