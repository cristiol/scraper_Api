# Generated by Django 4.2.1 on 2024-01-01 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("validator", "0005_rename_job_company_company_company"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="edited",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="job",
            name="published",
            field=models.BooleanField(default=False),
        ),
    ]
