# Generated by Django 5.1.2 on 2024-10-14 23:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id_brand', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id_category', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Obligatorio', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='productos.brand'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='productos.category'),
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('characteristics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.characteristics')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='characteristics',
            field=models.ManyToManyField(through='productos.Data', to='productos.characteristics'),
        ),
    ]
