# Generated by Django 4.2.9 on 2024-06-04 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='newsletter',
            name='job_wanted',
        ),
        migrations.RemoveField(
            model_name='newsletter',
            name='name',
        ),
        migrations.RemoveField(
            model_name='newsletter',
            name='searches',
        ),
        migrations.AddField(
            model_name='newsletter',
            name='company',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='job_title',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='job_type',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsletter.users'),
        ),
    ]