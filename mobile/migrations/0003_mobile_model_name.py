# Generated by Django 3.2 on 2021-12-25 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0002_auto_20211225_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobile',
            name='model_name',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='model', to='mobile.model_name'),
            preserve_default=False,
        ),
    ]
