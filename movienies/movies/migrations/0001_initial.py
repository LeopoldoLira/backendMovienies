# Generated by Django 4.2.1 on 2023-05-24 07:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=255, verbose_name="Movie's title")),
                ('movie_released_date', models.IntegerField(default=0)),
                ('movie_genre', models.CharField(max_length=255)),
                ('movie_plot', models.TextField(blank=True, null=True)),
                ('movie_image', models.ImageField(upload_to='')),
                ('movie_score', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('movie_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
