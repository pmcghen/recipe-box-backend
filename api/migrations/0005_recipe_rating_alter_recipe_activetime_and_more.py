# Generated by Django 4.0 on 2021-12-20 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_recipe_slug_alter_recipe_activetime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='rating',
            field=models.IntegerField(default=0, max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='activeTime',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='inactiveTime',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]