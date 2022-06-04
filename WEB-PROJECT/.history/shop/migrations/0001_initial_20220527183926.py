# Generated by Django 4.0.4 on 2022-05-27 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('close_image', models.ImageField(upload_to='')),
                ('goods_code', models.CharField(default='', max_length=50, verbose_name='number of goods')),
                ('name', models.CharField(max_length=100, verbose_name='name of goods')),
                ('goods_num', models.IntegerField(default=0, verbose_name='Inventory')),
                ('market_price', models.FloatField(default=0, verbose_name='market price')),
                ('shop_price', models.FloatField(default=0, verbose_name='shop price')),
                ('goods_brief', models.TextField(max_length=500, verbose_name='Product short description')),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(default='', max_length=11, verbose_name='phone number')),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(default='', max_length=11, verbose_name='phone number')),
                ('address', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(default=0, verbose_name='Purchase quantity')),
                ('pay_type', models.CharField(choices=[('cash', 'cash'), ('card', 'card'), ('paypal', 'paypal')], default='card', max_length=10, verbose_name='pay type')),
                ('order_mount', models.FloatField(default=0.0, verbose_name='order mount')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(default='', max_length=11, verbose_name='phone number')),
            ],
        ),
    ]
