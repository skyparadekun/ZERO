# Generated by Django 2.0.1 on 2018-11-27 00:16

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
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('content', models.TextField()),
                ('lastTime', models.DateTimeField(auto_now_add=True)),
                ('star', models.IntegerField(default=0)),
                ('auther', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastTime', models.DateTimeField(auto_now=True)),
                ('text', models.CharField(max_length=999)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funny.Article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=40)),
                ('director', models.CharField(max_length=40)),
                ('producer', models.CharField(max_length=20)),
                ('actor', models.CharField(max_length=40)),
                ('kind', models.CharField(max_length=20)),
                ('lastTime', models.TimeField()),
                ('length', models.IntegerField()),
                ('country', models.CharField(max_length=20)),
                ('language', models.CharField(max_length=15)),
                ('IMDb', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funny.Movie'),
        ),
    ]