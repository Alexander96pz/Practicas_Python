# Generated by Django 2.0.7 on 2021-08-20 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sumary',
            field=models.TextField(blank=True, null=True),
        ),
    ]
