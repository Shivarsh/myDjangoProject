# Generated by Django 4.2.6 on 2023-10-12 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('password', models.CharField(max_length=10)),
                ('cpassword', models.CharField(max_length=10)),
            ],
        ),
    ]
