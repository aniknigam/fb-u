# Generated by Django 3.1.6 on 2023-05-16 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20230516_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured_product',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3),
        ),
    ]
