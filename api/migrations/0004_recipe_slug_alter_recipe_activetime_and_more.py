# Generated by Django 4.0 on 2021-12-18 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_recipe_activetime_recipe_directions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='activeTime',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='directions',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='inactiveTime',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='notes',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
