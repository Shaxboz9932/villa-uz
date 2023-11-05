# Generated by Django 4.2.6 on 2023-10-31 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('villa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='allvilla',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='allvilla',
            name='area',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='allvilla',
            name='author_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='allvilla',
            name='author_phone_number',
            field=models.CharField(blank=True, max_length=13),
        ),
        migrations.AlterField(
            model_name='allvilla',
            name='bathrooms',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='allvilla',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='villa.category'),
        ),
        migrations.AlterField(
            model_name='allvilla',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='allvilla',
            name='floor',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='allvilla',
            name='parking',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='allvilla',
            name='price',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='allvilla',
            name='rooms',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='allvilla',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='allvilla',
            name='views',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=20, unique=True),
        ),
    ]
