# Generated by Django 2.1.1 on 2018-10-12 10:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_mysql.models.fields.bit


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('is_active', django_mysql.models.fields.bit.Bit1BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'ages',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('is_active', django_mysql.models.fields.bit.Bit1BooleanField(default=True)),
                ('home_url', models.URLField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'cities',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=1000)),
                ('mail', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'contacts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CrawledGuid',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('guid', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'crawled_guid',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('is_active', django_mysql.models.fields.bit.Bit1BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'licenses',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('api_id', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('is_active', django_mysql.models.fields.bit.Bit1BooleanField(default=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'lines',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Nursery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('is_active', django_mysql.models.fields.bit.Bit1BooleanField(default=True)),
                ('postcode', models.CharField(max_length=8)),
                ('address', models.CharField(max_length=255)),
                ('station_info', models.CharField(max_length=255, null=True)),
                ('url', models.URLField()),
                ('phone_number', models.CharField(max_length=15)),
                ('fax_number', models.CharField(max_length=15)),
                ('thumbnail_url', models.URLField()),
                ('latitude', models.DecimalField(decimal_places=9, max_digits=12)),
                ('longitude', models.DecimalField(decimal_places=9, max_digits=12)),
                ('open_time_weekday', models.CharField(max_length=255)),
                ('open_time_saturday', models.CharField(max_length=255)),
                ('close_day', models.CharField(max_length=1000)),
                ('accept_age', models.CharField(max_length=255)),
                ('stable_food_info', models.CharField(max_length=1000)),
                ('stable_food', django_mysql.models.fields.bit.Bit1BooleanField()),
                ('temporary_childcare', django_mysql.models.fields.bit.Bit1BooleanField()),
                ('overnight_childcare', django_mysql.models.fields.bit.Bit1BooleanField()),
                ('allday_childcare', django_mysql.models.fields.bit.Bit1BooleanField()),
                ('evaluation', django_mysql.models.fields.bit.Bit1BooleanField()),
                ('eco', django_mysql.models.fields.bit.Bit1BooleanField()),
                ('evaluation_url', models.URLField()),
                ('organizer', models.CharField(max_length=255)),
                ('event', models.CharField(max_length=1000)),
                ('service', models.CharField(max_length=1000)),
                ('policy', models.CharField(max_length=1000)),
                ('promise', models.CharField(max_length=1000)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'nurseries',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NurseryFreeNum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('free_num', models.IntegerField()),
                ('is_active', django_mysql.models.fields.bit.Bit1BooleanField(default=True)),
                ('modified_date', models.DateField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'nursery_free_nums',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NurseryScores',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.CharField(max_length=10)),
                ('score', models.IntegerField(default=None)),
                ('hierarchy', models.CharField(max_length=255)),
                ('note', models.CharField(max_length=255)),
                ('is_active', django_mysql.models.fields.bit.Bit1BooleanField(default=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'nursery_scores',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NurseryStatus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('free_num', models.IntegerField()),
                ('is_active', django_mysql.models.fields.bit.Bit1BooleanField(default=True)),
                ('modified_date', models.DateField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'nursery_status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SchoolType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('is_active', django_mysql.models.fields.bit.Bit1BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'school_types',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('api_id', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('is_active', django_mysql.models.fields.bit.Bit1BooleanField(default=True)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'stations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('home_url', models.URLField()),
                ('nursery_info_url', models.URLField()),
                ('nursery_free_num_info_url', models.URLField()),
                ('is_active', django_mysql.models.fields.bit.Bit1BooleanField(default=True)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'wards',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=255, null=True)),
                ('is_active', django_mysql.models.fields.bit.Bit1BooleanField(default=True)),
                ('is_admin', django_mysql.models.fields.bit.Bit1BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('child_age', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='infrastructure.Age')),
            ],
            options={
                'db_table': 'users',
                'managed': True,
            },
        ),
    ]
