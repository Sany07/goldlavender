# Generated by Django 3.2 on 2021-12-25 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0006_auto_20211225_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='brand_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='mobile.brand_name'),
        ),
    ]
