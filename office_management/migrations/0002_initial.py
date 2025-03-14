# Generated by Django 5.1.7 on 2025-03-14 08:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('office_management', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenancerequest',
            name='tenantId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='maintenancerequest',
            name='officeId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office_management.office'),
        ),
        migrations.AddField(
            model_name='rental',
            name='officeId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office_management.office'),
        ),
        migrations.AddField(
            model_name='rental',
            name='tenantId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='payment',
            name='rentalId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office_management.rental'),
        ),
    ]
