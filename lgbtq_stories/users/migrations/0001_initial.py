# Generated by Django 4.2.2 on 2023-06-18 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=12)),
                ('lname', models.CharField(max_length=12)),
                ('gender', models.CharField(choices=[('ML', 'Male'), ('FM', 'Female'), ('NB', 'Non-Binary'), ('PNTS', 'Prefer-Not-to-Say'), ('OTHR', 'Other')], default='PNTS', max_length=12)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('ph_num', models.IntegerField(max_length=10)),
            ],
        ),
    ]
