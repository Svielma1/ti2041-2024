# Generated by Django 5.1 on 2024-10-15 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_remove_characteristics_color_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='color',
        ),
        migrations.RemoveField(
            model_name='data',
            name='size',
        ),
        migrations.RemoveField(
            model_name='data',
            name='weight',
        ),
        migrations.AddField(
            model_name='characteristics',
            name='color',
            field=models.CharField(default='Por definir', max_length=50),
        ),
        migrations.AddField(
            model_name='characteristics',
            name='size',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='characteristics',
            name='weight',
            field=models.IntegerField(default=1),
        ),
    ]
