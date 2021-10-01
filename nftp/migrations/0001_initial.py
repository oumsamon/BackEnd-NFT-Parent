# Generated by Django 3.2.7 on 2021-09-23 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bottle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('photo_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BottleNipple',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('flow', models.CharField(max_length=100)),
                ('photo_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Diaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('photo_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DiaperComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newparent', models.CharField(max_length=100)),
                ('review', models.CharField(max_length=500)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DiaperComments', to='nftp.diaper')),
            ],
        ),
        migrations.CreateModel(
            name='BottleComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newparent', models.CharField(max_length=100)),
                ('review', models.CharField(max_length=500)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BottleComments', to='nftp.bottle')),
            ],
        ),
        migrations.CreateModel(
            name='BNComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newparent', models.CharField(max_length=100)),
                ('review', models.CharField(max_length=500)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BNComments', to='nftp.bottlenipple')),
            ],
        ),
    ]
