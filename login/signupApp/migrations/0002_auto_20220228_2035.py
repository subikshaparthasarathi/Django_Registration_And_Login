# Generated by Django 3.1.5 on 2022-02-28 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signupApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='password',
            new_name='pass1',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='phone',
            new_name='phonenumber',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='last_name',
            new_name='username',
        ),
        migrations.AddField(
            model_name='customer',
            name='pass2',
            field=models.CharField(default=models.CharField(max_length=500), max_length=500),
        ),
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
