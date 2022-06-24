# Generated by Django 4.0.5 on 2022-06-23 23:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pet', '0005_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('kind', models.CharField(blank=True, choices=[('Cat', 'cat'), ('Dog', 'dog'), ('Parrot', 'parrot'), ('Rabbit', 'Rabbit'), ('Guinea pig', 'guinea pig')], max_length=255)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Pet_owner',
        ),
    ]
