# Generated by Django 3.1.1 on 2021-02-22 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0003_auto_20210222_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='novidades',
            name='contato',
            field=models.CharField(default='3232323', max_length=20),
            preserve_default=False,
        ),
    ]
