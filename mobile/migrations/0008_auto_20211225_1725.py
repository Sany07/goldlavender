# Generated by Django 3.2 on 2021-12-25 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0007_alter_mobile_brand_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mobile_color', to='mobile.color'),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='model_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='model', to='mobile.model_name'),
        ),
    ]
