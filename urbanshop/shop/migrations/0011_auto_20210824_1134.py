# Generated by Django 3.2.4 on 2021-08-24 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20210823_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='tag',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ManyToManyField(related_name='images', to='shop.Image'),
        ),
    ]