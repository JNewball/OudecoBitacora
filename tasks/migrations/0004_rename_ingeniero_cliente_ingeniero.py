# Generated by Django 4.2 on 2023-04-14 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_cliente_ingeniero'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='ingeniero',
            new_name='Ingeniero',
        ),
    ]
