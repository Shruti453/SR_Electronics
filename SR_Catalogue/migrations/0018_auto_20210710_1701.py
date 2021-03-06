# Generated by Django 3.2.4 on 2021-07-10 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SR_Catalogue', '0017_auto_20210710_1516'),
    ]

    operations = [
        migrations.DeleteModel(
            name='logo',
        ),
        migrations.AlterField(
            model_name='display',
            name='Type_Of_Item',
            field=models.CharField(choices=[('/remote/0', 'Remote'), ('/IC_Transistor/0', 'IC Transistor'), ('/SoundSystem/0', 'Sound System'), ('/Extension/0', 'Extension'), ('/DiwaliLights/0', 'Diwali Lights'), ('/DTH/0', 'DTH'), ('/Miscellaneous/0', 'Miscellaneous'), ('/Leads/0', 'Leads'), ('/LED/0', 'LED'), ('', 'logo')], max_length=30),
        ),
        migrations.AlterField(
            model_name='diwali_light',
            name='Category',
            field=models.CharField(default='Diwali Lights', max_length=200),
        ),
        migrations.AlterField(
            model_name='dth',
            name='Category',
            field=models.CharField(default='DTH', max_length=200),
        ),
        migrations.AlterField(
            model_name='extension',
            name='Category',
            field=models.CharField(default='Extension', max_length=200),
        ),
        migrations.AlterField(
            model_name='ic_transistor',
            name='Category',
            field=models.CharField(default='IC & Transistors', max_length=200),
        ),
        migrations.AlterField(
            model_name='lead',
            name='Category',
            field=models.CharField(default='Leads', max_length=200),
        ),
        migrations.AlterField(
            model_name='led',
            name='Category',
            field=models.CharField(default='LED', max_length=200),
        ),
        migrations.AlterField(
            model_name='miscellaneous',
            name='Category',
            field=models.CharField(default='Miscellaneous', max_length=200),
        ),
        migrations.AlterField(
            model_name='remote',
            name='Category',
            field=models.CharField(default='Remote', max_length=200),
        ),
        migrations.AlterField(
            model_name='soundsystem',
            name='Category',
            field=models.CharField(default='Sound System', max_length=200),
        ),
    ]
