# Generated by Django 3.0.2 on 2020-01-14 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_movie_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('czas_trwania', models.ImageField(default=0, upload_to='')),
                ('rodzaj', models.ImageField(choices=[(1, 'Horror'), (4, 'Drama'), (2, 'Komedia'), (3, 'Sci-Fi'), (0, 'Nieznany')], default=0, upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='id',
        ),
        migrations.AlterField(
            model_name='movie',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='Filmy'),
        ),
        migrations.AddField(
            model_name='movie',
            name='info',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.ExtraInfo'),
            preserve_default=False,
        ),
    ]
