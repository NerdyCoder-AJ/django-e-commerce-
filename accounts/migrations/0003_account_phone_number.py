# Generated by Django 3.2.5 on 2021-08-16 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210807_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='phone_number',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]