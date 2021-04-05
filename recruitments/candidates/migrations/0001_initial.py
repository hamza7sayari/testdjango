# Generated by Django 3.1.7 on 2021-04-04 21:26

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_index=True, max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(db_index=True, max_length=30, verbose_name='las Name')),
                ('email', models.EmailField(db_index=True, max_length=100, verbose_name='Email')),
                ('birth_date', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='birthday')),
                ('phone_number', models.CharField(db_index=True, max_length=8, validators=[django.core.validators.MinLengthValidator(8)], verbose_name='Phone Number')),
                ('availability', models.FloatField(blank=True, db_index=True, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(0.6)], verbose_name='availability')),
                ('experience_years', models.FloatField(blank=True, db_index=True, null=True, validators=[django.core.validators.MinValueValidator(0.1)], verbose_name='availability')),
                ('curriculum_vitae', models.FileField(blank=True, db_index=True, default='', null=True, upload_to='candidates/', verbose_name='cv')),
                ('message', models.TextField(blank=True, db_index=True, null=True, verbose_name=' state of  job application ')),
                ('application_status', models.CharField(choices=[('in_progress_application', 'Application is in progress'), ('rejected_application', 'Sorry, application was rejected'), ('new_application', 'Create a new application'), ('confirmed_application', 'Application was confirmed')], db_index=True, default='new_application', max_length=45, verbose_name='Action Name')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
