# Generated by Django 3.1.4 on 2021-01-10 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm_admin', '0002_auto_20210110_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='crm_admin.country'),
        ),
    ]
