# Generated by Django 4.2.1 on 2024-02-10 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpageapp', '0005_remove_model_worker_or_not'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='worker_or_not',
            field=models.BooleanField(choices=[(1, 'worker'), (2, 'lazy')], default=1),
        ),
    ]
