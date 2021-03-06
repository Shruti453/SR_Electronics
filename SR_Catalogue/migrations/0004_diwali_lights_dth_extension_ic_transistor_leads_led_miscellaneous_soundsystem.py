# Generated by Django 3.2.4 on 2021-06-17 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SR_Catalogue', '0003_alter_remotes_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diwali_Lights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=50)),
                ('Category', models.CharField(default='Remote', max_length=50)),
                ('Price', models.IntegerField(default=0)),
                ('Quantity', models.IntegerField(default=0)),
                ('date', models.DateField()),
                ('Image', models.ImageField(upload_to='SR_Catalogue/images')),
            ],
        ),
        migrations.CreateModel(
            name='DTH',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=50)),
                ('Category', models.CharField(default='Remote', max_length=50)),
                ('Price', models.IntegerField(default=0)),
                ('Quantity', models.IntegerField(default=0)),
                ('date', models.DateField()),
                ('Image', models.ImageField(upload_to='SR_Catalogue/images')),
            ],
        ),
        migrations.CreateModel(
            name='Extension',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=50)),
                ('Category', models.CharField(default='Remote', max_length=50)),
                ('Price', models.IntegerField(default=0)),
                ('Quantity', models.IntegerField(default=0)),
                ('date', models.DateField()),
                ('Image', models.ImageField(upload_to='SR_Catalogue/images')),
            ],
        ),
        migrations.CreateModel(
            name='IC_Transistor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=50)),
                ('Category', models.CharField(default='Remote', max_length=50)),
                ('Price', models.IntegerField(default=0)),
                ('Quantity', models.IntegerField(default=0)),
                ('date', models.DateField()),
                ('Image', models.ImageField(upload_to='SR_Catalogue/images')),
            ],
        ),
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=50)),
                ('Category', models.CharField(default='Remote', max_length=50)),
                ('Price', models.IntegerField(default=0)),
                ('Quantity', models.IntegerField(default=0)),
                ('date', models.DateField()),
                ('Image', models.ImageField(upload_to='SR_Catalogue/images')),
            ],
        ),
        migrations.CreateModel(
            name='LED',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=50)),
                ('Category', models.CharField(default='Remote', max_length=50)),
                ('Price', models.IntegerField(default=0)),
                ('Quantity', models.IntegerField(default=0)),
                ('date', models.DateField()),
                ('Image', models.ImageField(upload_to='SR_Catalogue/images')),
            ],
        ),
        migrations.CreateModel(
            name='Miscellaneous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=50)),
                ('Category', models.CharField(default='Remote', max_length=50)),
                ('Price', models.IntegerField(default=0)),
                ('Quantity', models.IntegerField(default=0)),
                ('date', models.DateField()),
                ('Image', models.ImageField(upload_to='SR_Catalogue/images')),
            ],
        ),
        migrations.CreateModel(
            name='SoundSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=50)),
                ('Category', models.CharField(default='Remote', max_length=50)),
                ('Price', models.IntegerField(default=0)),
                ('Quantity', models.IntegerField(default=0)),
                ('date', models.DateField()),
                ('Image', models.ImageField(upload_to='SR_Catalogue/images')),
            ],
        ),
    ]
