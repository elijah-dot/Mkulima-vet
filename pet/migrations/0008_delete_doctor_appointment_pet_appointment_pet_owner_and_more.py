# Generated by Django 4.0.5 on 2022-06-23 23:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appointments', '0002_alter_appointment_doctors'),
        ('pet', '0007_appointment_vet'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.AddField(
            model_name='appointment',
            name='pet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pet.pet'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='pet_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='appointment',
            name='vet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='the_vet', to='pet.vet'),
        ),
    ]