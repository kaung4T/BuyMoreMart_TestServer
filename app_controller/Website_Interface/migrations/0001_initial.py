# Generated by Django 3.2.9 on 2023-06-01 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Four_IndexImageGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='website_interface')),
                ('image2', models.ImageField(upload_to='website_interface')),
                ('image3', models.ImageField(upload_to='website_interface')),
            ],
        ),
        migrations.CreateModel(
            name='One_IndexImageGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='website_interface')),
                ('image2', models.ImageField(upload_to='website_interface')),
                ('image3', models.ImageField(upload_to='website_interface')),
            ],
        ),
        migrations.CreateModel(
            name='Three_IndexImageGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='website_interface')),
                ('image2', models.ImageField(upload_to='website_interface')),
                ('image3', models.ImageField(upload_to='website_interface')),
            ],
        ),
        migrations.CreateModel(
            name='Two_IndexImageGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='website_interface')),
                ('image2', models.ImageField(upload_to='website_interface')),
                ('image3', models.ImageField(upload_to='website_interface')),
            ],
        ),
    ]