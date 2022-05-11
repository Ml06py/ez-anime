# Generated by Django 3.2.13 on 2022-05-08 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cast', '0002_auto_20220508_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='Movie-images')),
                ('name', models.CharField(max_length=20)),
                ('intro', models.TextField()),
                ('imdb', models.PositiveIntegerField(default=0)),
                ('seosons', models.PositiveIntegerField(default=0)),
                ('release_date', models.DateField()),
                ('actors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='film_actor', to='cast.cast')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='film_director', to='cast.cast')),
            ],
        ),
        migrations.CreateModel(
            name='seoson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seoson_number', models.PositiveIntegerField(default=1)),
                ('for_film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.film')),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='seoson_story',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.seoson'),
        ),
    ]