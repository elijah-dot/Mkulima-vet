# Generated by Django 4.0.5 on 2022-06-23 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0006_pet_delete_pet_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('service', models.CharField(choices=[('Grooming', 'Grooming'), ('Vaccination', 'Vaccination'), ('Diet and Nutrition', 'Diet and Nutrition'), ('Weight Mnagement', 'Weight Management'), ('Behavior', 'Behavior'), ('Oral and Dental Exam', 'Oral and Dental Exam'), (' Photoshoot', ' Photoshoot')], max_length=35)),
                ('time_booked', models.CharField(choices=[('0800hrs', '0800-0900'), ('0930hrs', '0930-1130'), ('noon', '1200-0130'), ('1400hrs', '0200-0300'), ('1530hrs', '0330-0430')], max_length=10)),
                ('when_the_booking_was_done', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('speciality', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='doctors/')),
            ],
        ),
    ]
