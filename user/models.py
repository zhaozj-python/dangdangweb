# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TAddress(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    postcode = models.CharField(max_length=6, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:

        db_table = 't_address'


class TBook(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=20, blank=True, null=True)
    book_cover = models.CharField(max_length=50, blank=True, null=True)
    intro = models.CharField(max_length=200, blank=True, null=True)
    comment = models.IntegerField(blank=True, null=True)
    author = models.CharField(max_length=20, blank=True, null=True)
    publish = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    price = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
    dang_price = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
    sales = models.IntegerField(blank=True, null=True)
    inventory = models.IntegerField(blank=True, null=True)
    store = models.CharField(max_length=30, blank=True, null=True)
    category = models.ForeignKey('TCategory', models.DO_NOTHING, blank=True, null=True)
    book_isbn = models.CharField(max_length=30, blank=True, null=True)
    word_count = models.IntegerField(blank=True, null=True)
    page_count = models.IntegerField(blank=True, null=True)
    format = models.IntegerField(blank=True, null=True)
    paper = models.CharField(max_length=20, blank=True, null=True)
    recommend = models.CharField(max_length=300, blank=True, null=True)
    author_intro = models.CharField(max_length=300, blank=True, null=True)
    menu = models.CharField(max_length=300, blank=True, null=True)
    comments = models.CharField(max_length=500, blank=True, null=True)

    def discount(self):
        return round(self.dang_price / self.price * 10, 2)

    class Meta:

        db_table = 't_book'


class TCart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    book = models.ForeignKey(TBook, models.DO_NOTHING, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 't_cart'


class TCategory(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    parentid = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 't_category'


class TOrder(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    order_name = models.CharField(max_length=30, blank=True, null=True)
    address = models.ForeignKey(TAddress, models.DO_NOTHING, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    order_id = models.CharField(max_length=30, blank=True, null=True)

    class Meta:

        db_table = 't_order'


class TOrderItem(models.Model):
    order = models.ForeignKey(TOrder, models.DO_NOTHING, blank=True, null=True)
    book = models.ForeignKey(TBook, models.DO_NOTHING, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 't_order_item'


class TUser(models.Model):
    username = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 't_user'
