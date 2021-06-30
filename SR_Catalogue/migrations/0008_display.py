# Generated by Django 3.2.4 on 2021-06-17 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SR_Catalogue', '0007_auto_20210617_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Display',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=50)),
                ('Image', models.ImageField(upload_to='SR_Catalogue/images')),
            ],
        ),
    ]