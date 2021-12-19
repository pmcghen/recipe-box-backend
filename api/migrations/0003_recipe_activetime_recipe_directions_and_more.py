# Generated by Django 4.0 on 2021-12-18 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='activeTime',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='recipe',
            name='directions',
            field=models.CharField(default=0, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='inactiveTime',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(default=0, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='notes',
            field=models.CharField(default=0, max_length=2000),
            preserve_default=False,
        ),
    ]
