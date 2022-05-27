# Generated by Django 3.2.4 on 2021-07-10 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SR_Catalogue', '0014_auto_20210618_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='SR_Catalogue/images')),
            ],
        ),
        migrations.RenameField(
            model_name='diwali_light',
            old_name='Image',
            new_name='Image1',
        ),
        migrations.RenameField(
            model_name='dth',
            old_name='Image',
            new_name='Image1',
        ),
        migrations.RenameField(
            model_name='extension',
            old_name='Image',
            new_name='Image1',
        ),
        migrations.RenameField(
            model_name='ic_transistor',
            old_name='Image',
            new_name='Image1',
        ),
        migrations.RenameField(
            model_name='lead',
            old_name='Image',
            new_name='Image1',
        ),
        migrations.RenameField(
            model_name='led',
            old_name='Image',
            new_name='Image1',
        ),
        migrations.RenameField(
            model_name='miscellaneous',
            old_name='Image',
            new_name='Image1',
        ),
        migrations.RenameField(
            model_name='remote',
            old_name='Image',
            new_name='Image1',
        ),
        migrations.RenameField(
            model_name='soundsystem',
            old_name='Image',
            new_name='Image1',
        ),
        migrations.RemoveField(
            model_name='diwali_light',
            name='Price',
        ),
        migrations.RemoveField(
            model_name='diwali_light',
            name='Quantity',
        ),
        migrations.RemoveField(
            model_name='dth',
            name='Price',
        ),
        migrations.RemoveField(
            model_name='dth',
            name='Quantity',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='Price',
        ),
        migrations.RemoveField(
            model_name='extension',
            name='Quantity',
        ),
        migrations.RemoveField(
            model_name='ic_transistor',
            name='Price',
        ),
        migrations.RemoveField(
            model_name='ic_transistor',
            name='Quantity',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='Price',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='Quantity',
        ),
        migrations.RemoveField(
            model_name='led',
            name='Price',
        ),
        migrations.RemoveField(
            model_name='led',
            name='Quantity',
        ),
        migrations.RemoveField(
            model_name='miscellaneous',
            name='Price',
        ),
        migrations.RemoveField(
            model_name='miscellaneous',
            name='Quantity',
        ),
        migrations.RemoveField(
            model_name='remote',
            name='Price',
        ),
        migrations.RemoveField(
            model_name='remote',
            name='Quantity',
        ),
        migrations.RemoveField(
            model_name='soundsystem',
            name='Price',
        ),
        migrations.RemoveField(
            model_name='soundsystem',
            name='Quantity',
        ),
        migrations.AddField(
            model_name='diwali_light',
            name='Image2',
            field=models.ImageField(null=True, upload_to='SR_Catalogue/images'),
        ),
        migrations.AddField(
            model_name='diwali_light',
            name='Image3',
            field=models.ImageField(null=True, upload_to='SR_Catalogue/images'),
        ),
        migrations.AddField(
            model_name='dth',
            name='Image2',
            field=models.ImageField(null=True, upload_to='SR_Catalogue/images'),
        ),
        migrations.AddField(
            model_name='dth',
            name='Image3',
            field=models.ImageField(null=True, upload_to='SR_Catalogue/images'),
        ),
        migrations.AddField(
            model_name='extension',
            name='Image2',
            field=models.ImageField(null=True, upload_to='SR_Catalogue/images'),
        ),
        migrations.AddField(
            model_name='extension',
            name='Image3',
            field=models.ImageField(null=True, upload_to='SR_Catalogue/images'),
        ),
        migrations.AddField(
            model_name='ic_transistor',
            name='Image2',
            field=models.ImageField(null=True, upload_to='SR_Catalogue/images'),
        ),
        migrations.AddField(
            model_name='ic_transistor',
            name='Image3',
            field=models.ImageField(null=True, upload_to='SR_Catalogue/images'),
        ),
        migrations.AddField(
            model_name='lead',
            name='Image2',
            field=models.ImageField(null=True, upload_to='SR_Catalogue/images'),
        ),
        migrations.AddField(
            model_name='lead',
            name='Image3',
            field=models.ImageField(null=True, upload_to='SR_Catalogue/images'),
        ),
        migrations.AddField(
            model_name='led',
            name='Image2',
            field=models.ImageField(null=True, upload_to='SR_Catalogue/images'),
        ),
        migrations.AddField(
            model_name='led',
            name='Image3',
            field=models.ImageField(null=True, upload_to='SR_Catalogue/images'),
        ),
        migrations.AddField(
            model_name='miscellaneous',
            name='Image2',
            field=models.ImageField(null=True, upload_to='SR_Catalogue/images'),
        ),
        migrations.AddField(
            model_name='miscellaneous',
            name='Image3',
            field=models.ImageField(null=True, upload_to='SR_Catalogue/images'),
        ),
        migrations.AddField(
            model_name='remote',
            name='Image2',
            field=models.ImageField(null=True, upload_to='SR_Catalogue/images'),
        ),
        migrations.AddField(
            model_name='remote',
            name='Image3',
            field=models.ImageField(null=True, upload_to='SR_Catalogue/images'),
        ),
        migrations.AddField(
            model_name='soundsystem',
            name='Image2',
            field=models.ImageField(null=True, upload_to='SR_Catalogue/images'),
        ),
        migrations.AddField(
            model_name='soundsystem',
            name='Image3',
            field=models.ImageField(null=True, upload_to='SR_Catalogue/images'),
        ),
    ]
