# Generated by Django 2.0.3 on 2018-03-31 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='product_age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='product_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='product_type',
            field=models.CharField(default='stationary', max_length=100),
        ),
    ]
