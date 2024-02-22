# Generated by Django 4.2.4 on 2024-02-01 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0013_alter_job_profile_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apply',
            old_name='website',
            new_name='portfolio',
        ),
        migrations.AlterField(
            model_name='apply',
            name='apply_job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apply', to='job.job'),
        ),
    ]
