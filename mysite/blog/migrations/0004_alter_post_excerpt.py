# Generated by Django 5.0.6 on 2024-06-09 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_options_post_excerpt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.TextField(null=True),
        ),
    ]
