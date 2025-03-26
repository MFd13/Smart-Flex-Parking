# Generated by Django 3.1.12 on 2025-03-19 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
        migrations.AddField(
            model_name='customuser',
            name='matricula',
            field=models.CharField(default='default_matricula', max_length=15, unique=True),
            preserve_default=False,
        ),
    ]
