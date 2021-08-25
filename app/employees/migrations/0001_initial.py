# Generated by Django 3.2.5 on 2021-08-25 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('age', models.IntegerField(default=18, verbose_name='Age')),
                ('password', models.CharField(max_length=50, verbose_name='Password')),
            ],
        ),
    ]