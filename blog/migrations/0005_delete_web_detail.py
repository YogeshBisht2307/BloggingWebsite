# Generated by Django 3.0.4 on 2021-02-07 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_seo_configuration_web_detail'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Web_detail',
        ),
    ]