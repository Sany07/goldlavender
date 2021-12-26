# Generated by Django 3.2 on 2021-12-26 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0009_auto_20211226_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mobile',
            name='color',
        ),
        migrations.AddField(
            model_name='mobile',
            name='color',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='mobile_color', to='mobile.color'),
            preserve_default=False,
        ),
    ]