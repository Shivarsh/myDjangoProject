# Generated by Django 4.2.6 on 2023-10-13 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_user_usertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=40)),
                ('product_price', models.CharField(max_length=10)),
                ('product_image', models.ImageField(upload_to='media/')),
                ('product_description', models.TextField()),
            ],
        ),
    ]