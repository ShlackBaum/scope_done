# Generated by Django 4.1 on 2022-08-29 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_scope_is_main'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
    ]
