# Generated by Django 4.0.3 on 2022-03-20 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tiempo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pronostico', models.CharField(max_length=200)),
                ('fecha', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
