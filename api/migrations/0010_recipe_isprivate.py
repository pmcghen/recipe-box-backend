# Generated by Django 4.0 on 2022-01-06 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_recipe_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='isPrivate',
            field=models.BooleanField(default=False),
        ),
    ]