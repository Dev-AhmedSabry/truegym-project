# Generated by Django 4.1.4 on 2022-12-31 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='', max_length=254)),
                ('city', models.CharField(choices=[('Cairo', 'Cairo'), ('Giza', 'Giza')], max_length=20)),
                ('area', models.CharField(choices=[('Nasr City', 'Nasr City'), ('Maadi', 'Maadi'), ('Doki', 'Doki'), ('Haram', 'Haram'), ('Faisal', 'Faisal'), ('6 October', '6 October')], max_length=30)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('gender', models.CharField(choices=[('Both', 'Both'), ('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('phone', models.CharField(blank=True, default='', max_length=11)),
                ('email', models.EmailField(blank=True, default='', max_length=100)),
                ('image', models.ImageField(blank=True, default='', upload_to='gym/')),
                ('review', models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], max_length=2, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('is_phone_verified', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]