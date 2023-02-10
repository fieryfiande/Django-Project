# Generated by Django 4.1.6 on 2023-02-10 06:36

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
            name='order',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('purchase_id', models.IntegerField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('dev_type', models.CharField(max_length=100)),
                ('order_status', models.CharField(choices=[('Pending', 'Pending'), ('In-Transit', 'In-Transit'), ('Delivered', 'Delivered')], max_length=100)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_createdby', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updatedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='site',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('site_id', models.IntegerField(primary_key=True, serialize=False)),
                ('site_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField(null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_createdby', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updatedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='switch',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('serial_no', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('ip_address', models.CharField(max_length=100)),
                ('mac_address', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('status', models.BooleanField()),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_createdby', to=settings.AUTH_USER_MODEL)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='switchorder', to='central_inventory.order')),
                ('site_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='switchpersite', to='central_inventory.site')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updatedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='iap',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('serial_no', models.IntegerField(primary_key=True, serialize=False)),
                ('ip_address', models.CharField(max_length=100)),
                ('mac_address', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('status', models.BooleanField()),
                ('is_vc', models.BooleanField()),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_createdby', to=settings.AUTH_USER_MODEL)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='iaporder', to='central_inventory.order')),
                ('site_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='iappersite', to='central_inventory.site')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_updatedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
