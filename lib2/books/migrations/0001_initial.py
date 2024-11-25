# Generated by Django 5.1 on 2024-10-03 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=20)),
                ('pages', models.IntegerField()),
                ('price', models.IntegerField()),
                ('language', models.CharField(max_length=30)),
                ('cover', models.ImageField(upload_to='images')),
                ('pdf', models.FileField(upload_to='pdf')),
            ],
        ),
    ]
