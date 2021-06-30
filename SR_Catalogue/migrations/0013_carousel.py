# Generated by Django 3.2.4 on 2021-06-18 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SR_Catalogue', '0012_alter_display_type_of_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=50)),
                ('Image', models.ImageField(upload_to='SR_Catalogue/images')),
            ],
        ),
    ]