# Generated by Django 5.1.1 on 2024-09-22 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_tbl_category_tbl_register_tbl_slider_tbl_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=50, null=True)),
                ('product_id', models.IntegerField()),
                ('product_image', models.CharField(max_length=200, null=True)),
                ('product_price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('total_price', models.FloatField()),
                ('product_name', models.CharField(max_length=100, null=True)),
                ('added_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=50, null=True)),
                ('product_id', models.IntegerField()),
                ('product_name', models.CharField(max_length=100, null=True)),
                ('product_image', models.CharField(max_length=200, null=True)),
                ('product_price', models.FloatField()),
                ('product_quantity', models.IntegerField()),
                ('total_price', models.FloatField()),
                ('status', models.CharField(max_length=15, null=True)),
                ('order_date', models.DateField(null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='tbl_register',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='tbl_register',
            old_name='City',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='tbl_register',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='tbl_register',
            old_name='Mobile',
            new_name='mobile',
        ),
        migrations.RenameField(
            model_name='tbl_register',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='tbl_register',
            old_name='Password',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='tbl_register',
            old_name='Picture',
            new_name='picture',
        ),
        migrations.RenameField(
            model_name='tbl_register',
            old_name='Pincode',
            new_name='pincode',
        ),
    ]
