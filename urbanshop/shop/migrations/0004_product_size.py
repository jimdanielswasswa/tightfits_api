# Generated by Django 3.2.4 on 2021-08-13 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_sale_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shop.size'),
        ),
    ]