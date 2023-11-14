# Generated by Django 4.2.6 on 2023-11-13 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='ages',
            field=models.CharField(choices=[('0+', '0+'), ('6+', '6+'), ('12+', '12+'), ('14+', '14+'), ('16+', '16+'), ('18+', '18+')], default='0+', max_length=3),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Название'),
        ),
    ]