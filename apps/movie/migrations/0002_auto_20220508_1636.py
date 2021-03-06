# Generated by Django 3.2.13 on 2022-05-08 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cast', '0003_auto_20220508_1632'),
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='actors',
        ),
        migrations.AddField(
            model_name='film',
            name='actors',
            field=models.ManyToManyField(related_name='film_actor', to='cast.Cast'),
        ),
        migrations.RemoveField(
            model_name='film',
            name='director',
        ),
        migrations.AddField(
            model_name='film',
            name='director',
            field=models.ManyToManyField(related_name='film_director', to='cast.Cast'),
        ),
        migrations.RemoveField(
            model_name='film',
            name='seoson_story',
        ),
        migrations.AddField(
            model_name='film',
            name='seoson_story',
            field=models.ManyToManyField(blank=True, null=True, to='movie.seoson'),
        ),
    ]
