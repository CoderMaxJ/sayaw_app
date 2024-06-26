# Generated by Django 5.0.3 on 2024-03-11 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(max_length=20, null=True)),
                ('is_fully_paid', models.BooleanField(default=False, null=True)),
                ('is_paid', models.BooleanField(default=False, null=True)),
                ('is_cancellation_approve', models.BooleanField(default=False, null=True)),
                ('is_cancel', models.BooleanField(default=False)),
                ('transaction_Code', models.CharField(max_length=10, null=True)),
                ('date_Reserved', models.DateField(null=True)),
                ('time_Reserved', models.TimeField(null=True)),
                ('guest_Name', models.CharField(max_length=30, null=True)),
                ('guest_Lastname', models.CharField(max_length=30, null=True)),
                ('guest_Address', models.CharField(max_length=50, null=True)),
                ('guest_Number', models.IntegerField(null=True)),
                ('cottage_number', models.IntegerField(null=True)),
                ('cottage_price', models.IntegerField(null=True)),
                ('room_number', models.IntegerField(null=True)),
                ('gate_Number', models.CharField(max_length=50, null=True)),
                ('room_Price', models.IntegerField(null=True)),
                ('date_In', models.DateField(null=True)),
                ('date_Out', models.DateField(null=True)),
                ('stay_Duration', models.IntegerField(null=True)),
                ('time_In', models.TimeField(null=True)),
                ('time_Out', models.TimeField(null=True)),
                ('feedback', models.TextField(max_length=200, null=True)),
                ('partial_paid', models.IntegerField(default=0)),
                ('total_bill', models.IntegerField(default=0)),
                ('balance_bill', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='cottages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_availlable', models.BooleanField(default=False)),
                ('gate_number', models.CharField(max_length=10, null=True)),
                ('cottage_number', models.IntegerField(null=True)),
                ('cottage_price', models.IntegerField(null=True)),
                ('front_view', models.ImageField(null=True, upload_to='cottage_image/')),
                ('inside_view1', models.ImageField(null=True, upload_to='cottage_image/')),
                ('inside_view2', models.ImageField(null=True, upload_to='cottage_image/')),
                ('inside_view3', models.ImageField(null=True, upload_to='cottage_image/')),
                ('cottage_description', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='gcash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Guest_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_name', models.CharField(max_length=100, null=True)),
                ('guest_lastname', models.CharField(max_length=100, null=True)),
                ('guest_address', models.CharField(max_length=100, null=True)),
                ('room', models.CharField(max_length=100, null=True)),
                ('cottage', models.CharField(max_length=100, null=True)),
                ('program', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=100, null=True)),
                ('total_bill', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='message_storage_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='message_storage_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='message_storage_3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='nationality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_nationality', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='paid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_name', models.CharField(max_length=100)),
                ('guest_lastname', models.CharField(max_length=100, null=True)),
                ('payment_proof', models.ImageField(upload_to='payment_proof/')),
                ('transaction_code', models.CharField(max_length=10)),
                ('date_paid', models.DateField(null=True)),
                ('time_paid', models.TimeField(null=True)),
                ('total_bill', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='paymaya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_availlable', models.BooleanField(default=True)),
                ('gate_number', models.CharField(max_length=10, null=True)),
                ('room_number', models.IntegerField(null=True)),
                ('room_price', models.IntegerField(null=True)),
                ('front_view', models.ImageField(null=True, upload_to='room_image/')),
                ('inside_view1', models.ImageField(null=True, upload_to='room_image/')),
                ('inside_view2', models.ImageField(null=True, upload_to='room_image/')),
                ('inside_view3', models.ImageField(null=True, upload_to='room_image/')),
                ('room_description', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
