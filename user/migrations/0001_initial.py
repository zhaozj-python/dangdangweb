# Generated by Django 2.0.6 on 2020-09-17 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('postcode', models.CharField(blank=True, max_length=6, null=True)),
                ('telephone', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 't_address',
            },
        ),
        migrations.CreateModel(
            name='TBook',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(blank=True, max_length=20, null=True)),
                ('book_cover', models.CharField(blank=True, max_length=50, null=True)),
                ('intro', models.CharField(blank=True, max_length=200, null=True)),
                ('comment', models.IntegerField(blank=True, null=True)),
                ('author', models.CharField(blank=True, max_length=20, null=True)),
                ('publish', models.CharField(blank=True, max_length=20, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=0, max_digits=11, null=True)),
                ('dang_price', models.DecimalField(blank=True, decimal_places=0, max_digits=11, null=True)),
                ('sales', models.IntegerField(blank=True, null=True)),
                ('inventory', models.IntegerField(blank=True, null=True)),
                ('store', models.CharField(blank=True, max_length=30, null=True)),
                ('book_isbn', models.CharField(blank=True, max_length=30, null=True)),
                ('word_count', models.IntegerField(blank=True, null=True)),
                ('page_count', models.IntegerField(blank=True, null=True)),
                ('format', models.IntegerField(blank=True, null=True)),
                ('paper', models.CharField(blank=True, max_length=20, null=True)),
                ('recommend', models.CharField(blank=True, max_length=300, null=True)),
                ('author_intro', models.CharField(blank=True, max_length=300, null=True)),
                ('menu', models.CharField(blank=True, max_length=300, null=True)),
                ('comments', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 't_book',
            },
        ),
        migrations.CreateModel(
            name='TCart',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('count', models.IntegerField(blank=True, null=True)),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.TBook')),
            ],
            options={
                'db_table': 't_cart',
            },
        ),
        migrations.CreateModel(
            name='TCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('parentid', models.IntegerField(blank=True, null=True)),
                ('level', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_category',
            },
        ),
        migrations.CreateModel(
            name='TOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order_name', models.CharField(blank=True, max_length=30, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('order_id', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.TAddress')),
            ],
            options={
                'db_table': 't_order',
            },
        ),
        migrations.CreateModel(
            name='TOrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(blank=True, null=True)),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.TBook')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.TOrder')),
            ],
            options={
                'db_table': 't_order_item',
            },
        ),
        migrations.CreateModel(
            name='TUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=20, null=True)),
                ('password', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 't_user',
            },
        ),
        migrations.AddField(
            model_name='torder',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.TUser'),
        ),
        migrations.AddField(
            model_name='tcart',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.TUser'),
        ),
        migrations.AddField(
            model_name='tbook',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.TCategory'),
        ),
        migrations.AddField(
            model_name='taddress',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.TUser'),
        ),
    ]
