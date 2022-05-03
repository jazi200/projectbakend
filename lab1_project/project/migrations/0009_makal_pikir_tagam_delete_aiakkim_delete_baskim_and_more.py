# Generated by Django 4.0.2 on 2022-03-03 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_rename_articles_aiakkim_rename_work_baskim_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Makal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True)),
                ('title', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Pikir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tagam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Aiakkim',
        ),
        migrations.DeleteModel(
            name='Baskim',
        ),
        migrations.DeleteModel(
            name='Surtkim',
        ),
    ]
