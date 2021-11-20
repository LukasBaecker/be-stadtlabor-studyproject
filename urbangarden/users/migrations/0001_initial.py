# Generated by Django 3.1 on 2021-11-20 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gardens', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Privilege',
            fields=[
                ('privilege_id', models.AutoField(primary_key=True, serialize=False)),
                ('privilege_name', models.CharField(choices=[('ADMIN', 'Admin'), ('USER', 'User')], default='USER', max_length=50)),
                ('privilege_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('is_logged_in', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('garden', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='gardens.garden')),
                ('privilege', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='users.privilege')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
