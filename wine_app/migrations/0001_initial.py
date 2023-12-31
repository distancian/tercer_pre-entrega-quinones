# Generated by Django 4.2.5 on 2023-09-12 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.IntegerField()),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=40)),
                ('precio', models.IntegerField()),
                ('categoria', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='vendedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=40)),
                ('precio', models.IntegerField()),
                ('categoria', models.CharField(max_length=40)),
            ],
        ),
    ]
