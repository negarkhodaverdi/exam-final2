# Generated by Django 4.2.6 on 2023-10-30 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carts',
            name='ip',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AddField(
            model_name='carts',
            name='price',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='carts',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.products'),
        ),
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(null=True, upload_to='static/Products'),
        ),
    ]
