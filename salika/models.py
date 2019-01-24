# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create,
#   modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field
# names.
from django.db import models
# from haystack import indexes


class Actor(models.Model):
    actor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField()

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        managed = False
        db_table = 'actor'


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=20)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=20)
    last_update = models.DateTimeField()

    def __str__(self):
        return '%s, %s' % (self.address, self.district)

    class Meta:
        managed = False
        db_table = 'address'
        verbose_name_plural = 'Addresses'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, on_delete=models.CASCADE)
    permission = models.ForeignKey('AuthPermission', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', on_delete=models.CASCADE)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    def __str__(self):
        return '%s' % self.username

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    group = models.ForeignKey(AuthGroup, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    permission = models.ForeignKey(AuthPermission, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    last_update = models.DateTimeField()

    def __str__(self):
        return '%s' % self.name

    class Meta:
        managed = False
        db_table = 'category'
        verbose_name_plural = "Categories"


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    last_update = models.DateTimeField()

    def __str__(self):
        return '%s' % self.city

    class Meta:
        managed = False
        db_table = 'city'
        verbose_name_plural = "Cities"


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50)
    last_update = models.DateTimeField()

    def __str__(self):
        return '%s' % self.country

    class Meta:
        managed = False
        db_table = 'country'
        verbose_name_plural = "Countries"


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    store_id = models.SmallIntegerField()
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=50, blank=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    activebool = models.BooleanField()
    create_date = models.DateField()
    last_update = models.DateTimeField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        managed = False
        db_table = 'customer'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', on_delete=models.CASCADE,
                                     blank=True, null=True)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
        verbose_name_plural = 'Django migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Film(models.Model):
    film_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)
    rental_duration = models.SmallIntegerField()
    rental_rate = models.DecimalField(max_digits=4, decimal_places=2)
    length = models.SmallIntegerField(blank=True, null=True)
    replacement_cost = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.TextField(blank=True,
                              null=True)  # This field type is a guess.
    last_update = models.DateTimeField()
    special_features = models.TextField(blank=True,
                                        null=True)
    fulltext = models.TextField()  # This field type is a guess.

    def __str__(self):
        return '%s' % self.title

    class Meta:
        managed = False
        db_table = 'film'


class FilmActor(models.Model):
    actor_id = models.ForeignKey(Actor, on_delete=models.CASCADE,
                                 db_column='actor_id')
    film_id = models.OneToOneField(Film, on_delete=models.CASCADE,
                                   db_column='film_id', primary_key=True)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'film_actor'
        unique_together = (('actor_id', 'film_id'),)


class FilmCategory(models.Model):
    film_id = models.OneToOneField(Film, on_delete=models.CASCADE,
                                   db_column='film_id', primary_key=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE,
                                    db_column='category_id')
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'film_category'
        unique_together = (('film_id', 'category_id'),)
        verbose_name_plural = "Film categories"


class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    store_id = models.SmallIntegerField()
    last_update = models.DateTimeField()

    def __str__(self):
        return '%s from Store#' % self.film.title + ' ' + str(self.store_id)

    class Meta:
        managed = False
        db_table = 'inventory'
        verbose_name_plural = 'Inventories'


class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_update = models.DateTimeField()

    def __str__(self):
        return '%s' % self.name

    class Meta:
        managed = False
        db_table = 'language'


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    staff = models.ForeignKey('Staff', on_delete=models.CASCADE)
    rental = models.ForeignKey('Rental', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    payment_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'payment'


class Rental(models.Model):
    rental_id = models.AutoField(primary_key=True)
    rental_date = models.DateTimeField()
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    return_date = models.DateTimeField(blank=True, null=True)
    staff = models.ForeignKey('Staff', on_delete=models.CASCADE)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rental'
        unique_together = (('rental_date', 'inventory', 'customer'),)


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    email = models.CharField(max_length=50, blank=True, null=True)
    store_id = models.SmallIntegerField()
    active = models.BooleanField()
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=40, blank=True, null=True)
    last_update = models.DateTimeField()
    picture = models.BinaryField()

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        managed = False
        db_table = 'staff'


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    manager_staff = models.OneToOneField(Staff, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'store'
