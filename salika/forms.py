from django import forms
from .models import Actor, Address, AuthGroup, AuthGroupPermissions, \
    AuthPermission, AuthUser, AuthUserGroups, AuthUserUserPermissions, \
    Category, City, Country, Customer, DjangoAdminLog, DjangoContentType, \
    DjangoMigrations, DjangoSession, Film, FilmActor, FilmCategory, Inventory, \
    Language, Payment, Rental, Staff, Store


class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ['actor_id', 'first_name', 'last_name', 'last_update']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(ActorForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(ActorForm, self).is_valid()

    def full_clean(self):
        return super(ActorForm, self).full_clean()

    def clean_actor_id(self):
        actor_id = self.cleaned_data.get("actor_id", None)
        return actor_id

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name", None)
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name", None)
        return last_name

    def clean_last_update(self):
        last_update = self.cleaned_data.get("last_update", None)
        return last_update

    def clean(self):
        return super(ActorForm, self).clean()

    def validate_unique(self):
        return super(ActorForm, self).validate_unique()

    def save(self, commit=True):
        return super(ActorForm, self).save(commit)


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address_id', 'address', 'address2', 'district', 'city',
                  'postal_code', 'phone', 'last_update']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(AddressForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(AddressForm, self).is_valid()

    def full_clean(self):
        return super(AddressForm, self).full_clean()

    def clean_address_id(self):
        address_id = self.cleaned_data.get("address_id", None)
        return address_id

    def clean_address(self):
        address = self.cleaned_data.get("address", None)
        return address

    def clean_address2(self):
        address2 = self.cleaned_data.get("address2", None)
        return address2

    def clean_district(self):
        district = self.cleaned_data.get("district", None)
        return district

    def clean_city(self):
        city = self.cleaned_data.get("city", None)
        return city

    def clean_postal_code(self):
        postal_code = self.cleaned_data.get("postal_code", None)
        return postal_code

    def clean_phone(self):
        phone = self.cleaned_data.get("phone", None)
        return phone

    def clean_last_update(self):
        last_update = self.cleaned_data.get("last_update", None)
        return last_update

    def clean(self):
        return super(AddressForm, self).clean()

    def validate_unique(self):
        return super(AddressForm, self).validate_unique()

    def save(self, commit=True):
        return super(AddressForm, self).save(commit)


class AuthGroupForm(forms.ModelForm):
    class Meta:
        model = AuthGroup
        fields = ['name']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(AuthGroupForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(AuthGroupForm, self).is_valid()

    def full_clean(self):
        return super(AuthGroupForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean(self):
        return super(AuthGroupForm, self).clean()

    def validate_unique(self):
        return super(AuthGroupForm, self).validate_unique()

    def save(self, commit=True):
        return super(AuthGroupForm, self).save(commit)


class AuthGroupPermissionsForm(forms.ModelForm):
    class Meta:
        model = AuthGroupPermissions
        fields = ['group', 'permission']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(AuthGroupPermissionsForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(AuthGroupPermissionsForm, self).is_valid()

    def full_clean(self):
        return super(AuthGroupPermissionsForm, self).full_clean()

    def clean_group(self):
        group = self.cleaned_data.get("group", None)
        return group

    def clean_permission(self):
        permission = self.cleaned_data.get("permission", None)
        return permission

    def clean(self):
        return super(AuthGroupPermissionsForm, self).clean()

    def validate_unique(self):
        return super(AuthGroupPermissionsForm, self).validate_unique()

    def save(self, commit=True):
        return super(AuthGroupPermissionsForm, self).save(commit)


class AuthPermissionForm(forms.ModelForm):
    class Meta:
        model = AuthPermission
        fields = ['name', 'content_type', 'codename']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(AuthPermissionForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(AuthPermissionForm, self).is_valid()

    def full_clean(self):
        return super(AuthPermissionForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_content_type(self):
        content_type = self.cleaned_data.get("content_type", None)
        return content_type

    def clean_codename(self):
        codename = self.cleaned_data.get("codename", None)
        return codename

    def clean(self):
        return super(AuthPermissionForm, self).clean()

    def validate_unique(self):
        return super(AuthPermissionForm, self).validate_unique()

    def save(self, commit=True):
        return super(AuthPermissionForm, self).save(commit)


class AuthUserForm(forms.ModelForm):
    class Meta:
        model = AuthUser
        fields = ['password', 'last_login', 'is_superuser', 'username',
                  'first_name', 'last_name', 'email', 'is_staff', 'is_active',
                  'date_joined']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(AuthUserForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(AuthUserForm, self).is_valid()

    def full_clean(self):
        return super(AuthUserForm, self).full_clean()

    def clean_password(self):
        password = self.cleaned_data.get("password", None)
        return password

    def clean_last_login(self):
        last_login = self.cleaned_data.get("last_login", None)
        return last_login

    def clean_is_superuser(self):
        is_superuser = self.cleaned_data.get("is_superuser", None)
        return is_superuser

    def clean_username(self):
        username = self.cleaned_data.get("username", None)
        return username

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name", None)
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name", None)
        return last_name

    def clean_email(self):
        email = self.cleaned_data.get("email", None)
        return email

    def clean_is_staff(self):
        is_staff = self.cleaned_data.get("is_staff", None)
        return is_staff

    def clean_is_active(self):
        is_active = self.cleaned_data.get("is_active", None)
        return is_active

    def clean_date_joined(self):
        date_joined = self.cleaned_data.get("date_joined", None)
        return date_joined

    def clean(self):
        return super(AuthUserForm, self).clean()

    def validate_unique(self):
        return super(AuthUserForm, self).validate_unique()

    def save(self, commit=True):
        return super(AuthUserForm, self).save(commit)


class AuthUserGroupsForm(forms.ModelForm):
    class Meta:
        model = AuthUserGroups
        fields = ['user', 'group']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(AuthUserGroupsForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(AuthUserGroupsForm, self).is_valid()

    def full_clean(self):
        return super(AuthUserGroupsForm, self).full_clean()

    def clean_user(self):
        user = self.cleaned_data.get("user", None)
        return user

    def clean_group(self):
        group = self.cleaned_data.get("group", None)
        return group

    def clean(self):
        return super(AuthUserGroupsForm, self).clean()

    def validate_unique(self):
        return super(AuthUserGroupsForm, self).validate_unique()

    def save(self, commit=True):
        return super(AuthUserGroupsForm, self).save(commit)


class AuthUserUserPermissionsForm(forms.ModelForm):
    class Meta:
        model = AuthUserUserPermissions
        fields = ['user', 'permission']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(AuthUserUserPermissionsForm, self).__init__(*args,
                                                                 **kwargs)

    def is_valid(self):
        return super(AuthUserUserPermissionsForm, self).is_valid()

    def full_clean(self):
        return super(AuthUserUserPermissionsForm, self).full_clean()

    def clean_user(self):
        user = self.cleaned_data.get("user", None)
        return user

    def clean_permission(self):
        permission = self.cleaned_data.get("permission", None)
        return permission

    def clean(self):
        return super(AuthUserUserPermissionsForm, self).clean()

    def validate_unique(self):
        return super(AuthUserUserPermissionsForm, self).validate_unique()

    def save(self, commit=True):
        return super(AuthUserUserPermissionsForm, self).save(commit)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_id', 'name', 'last_update']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(CategoryForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(CategoryForm, self).is_valid()

    def full_clean(self):
        return super(CategoryForm, self).full_clean()

    def clean_category_id(self):
        category_id = self.cleaned_data.get("category_id", None)
        return category_id

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_last_update(self):
        last_update = self.cleaned_data.get("last_update", None)
        return last_update

    def clean(self):
        return super(CategoryForm, self).clean()

    def validate_unique(self):
        return super(CategoryForm, self).validate_unique()

    def save(self, commit=True):
        return super(CategoryForm, self).save(commit)


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['city_id', 'city', 'country', 'last_update']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(CityForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(CityForm, self).is_valid()

    def full_clean(self):
        return super(CityForm, self).full_clean()

    def clean_city_id(self):
        city_id = self.cleaned_data.get("city_id", None)
        return city_id

    def clean_city(self):
        city = self.cleaned_data.get("city", None)
        return city

    def clean_country(self):
        country = self.cleaned_data.get("country", None)
        return country

    def clean_last_update(self):
        last_update = self.cleaned_data.get("last_update", None)
        return last_update

    def clean(self):
        return super(CityForm, self).clean()

    def validate_unique(self):
        return super(CityForm, self).validate_unique()

    def save(self, commit=True):
        return super(CityForm, self).save(commit)


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['country_id', 'country', 'last_update']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(CountryForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(CountryForm, self).is_valid()

    def full_clean(self):
        return super(CountryForm, self).full_clean()

    def clean_country_id(self):
        country_id = self.cleaned_data.get("country_id", None)
        return country_id

    def clean_country(self):
        country = self.cleaned_data.get("country", None)
        return country

    def clean_last_update(self):
        last_update = self.cleaned_data.get("last_update", None)
        return last_update

    def clean(self):
        return super(CountryForm, self).clean()

    def validate_unique(self):
        return super(CountryForm, self).validate_unique()

    def save(self, commit=True):
        return super(CountryForm, self).save(commit)


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_id', 'store_id', 'first_name', 'last_name',
                  'email', 'address', 'activebool', 'create_date',
                  'last_update', 'active']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(CustomerForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(CustomerForm, self).is_valid()

    def full_clean(self):
        return super(CustomerForm, self).full_clean()

    def clean_customer_id(self):
        customer_id = self.cleaned_data.get("customer_id", None)
        return customer_id

    def clean_store_id(self):
        store_id = self.cleaned_data.get("store_id", None)
        return store_id

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name", None)
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name", None)
        return last_name

    def clean_email(self):
        email = self.cleaned_data.get("email", None)
        return email

    def clean_address(self):
        address = self.cleaned_data.get("address", None)
        return address

    def clean_activebool(self):
        activebool = self.cleaned_data.get("activebool", None)
        return activebool

    def clean_create_date(self):
        create_date = self.cleaned_data.get("create_date", None)
        return create_date

    def clean_last_update(self):
        last_update = self.cleaned_data.get("last_update", None)
        return last_update

    def clean_active(self):
        active = self.cleaned_data.get("active", None)
        return active

    def clean(self):
        return super(CustomerForm, self).clean()

    def validate_unique(self):
        return super(CustomerForm, self).validate_unique()

    def save(self, commit=True):
        return super(CustomerForm, self).save(commit)


class DjangoAdminLogForm(forms.ModelForm):
    class Meta:
        model = DjangoAdminLog
        fields = ['action_time', 'object_id', 'object_repr', 'action_flag',
                  'change_message', 'content_type', 'user']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(DjangoAdminLogForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(DjangoAdminLogForm, self).is_valid()

    def full_clean(self):
        return super(DjangoAdminLogForm, self).full_clean()

    def clean_action_time(self):
        action_time = self.cleaned_data.get("action_time", None)
        return action_time

    def clean_object_id(self):
        object_id = self.cleaned_data.get("object_id", None)
        return object_id

    def clean_object_repr(self):
        object_repr = self.cleaned_data.get("object_repr", None)
        return object_repr

    def clean_action_flag(self):
        action_flag = self.cleaned_data.get("action_flag", None)
        return action_flag

    def clean_change_message(self):
        change_message = self.cleaned_data.get("change_message", None)
        return change_message

    def clean_content_type(self):
        content_type = self.cleaned_data.get("content_type", None)
        return content_type

    def clean_user(self):
        user = self.cleaned_data.get("user", None)
        return user

    def clean(self):
        return super(DjangoAdminLogForm, self).clean()

    def validate_unique(self):
        return super(DjangoAdminLogForm, self).validate_unique()

    def save(self, commit=True):
        return super(DjangoAdminLogForm, self).save(commit)


class DjangoContentTypeForm(forms.ModelForm):
    class Meta:
        model = DjangoContentType
        fields = ['app_label', 'model']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(DjangoContentTypeForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(DjangoContentTypeForm, self).is_valid()

    def full_clean(self):
        return super(DjangoContentTypeForm, self).full_clean()

    def clean_app_label(self):
        app_label = self.cleaned_data.get("app_label", None)
        return app_label

    def clean_model(self):
        model = self.cleaned_data.get("model", None)
        return model

    def clean(self):
        return super(DjangoContentTypeForm, self).clean()

    def validate_unique(self):
        return super(DjangoContentTypeForm, self).validate_unique()

    def save(self, commit=True):
        return super(DjangoContentTypeForm, self).save(commit)


class DjangoMigrationsForm(forms.ModelForm):
    class Meta:
        model = DjangoMigrations
        fields = ['app', 'name', 'applied']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(DjangoMigrationsForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(DjangoMigrationsForm, self).is_valid()

    def full_clean(self):
        return super(DjangoMigrationsForm, self).full_clean()

    def clean_app(self):
        app = self.cleaned_data.get("app", None)
        return app

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_applied(self):
        applied = self.cleaned_data.get("applied", None)
        return applied

    def clean(self):
        return super(DjangoMigrationsForm, self).clean()

    def validate_unique(self):
        return super(DjangoMigrationsForm, self).validate_unique()

    def save(self, commit=True):
        return super(DjangoMigrationsForm, self).save(commit)


class DjangoSessionForm(forms.ModelForm):
    class Meta:
        model = DjangoSession
        fields = ['session_key', 'session_data', 'expire_date']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(DjangoSessionForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(DjangoSessionForm, self).is_valid()

    def full_clean(self):
        return super(DjangoSessionForm, self).full_clean()

    def clean_session_key(self):
        session_key = self.cleaned_data.get("session_key", None)
        return session_key

    def clean_session_data(self):
        session_data = self.cleaned_data.get("session_data", None)
        return session_data

    def clean_expire_date(self):
        expire_date = self.cleaned_data.get("expire_date", None)
        return expire_date

    def clean(self):
        return super(DjangoSessionForm, self).clean()

    def validate_unique(self):
        return super(DjangoSessionForm, self).validate_unique()

    def save(self, commit=True):
        return super(DjangoSessionForm, self).save(commit)


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['film_id', 'title', 'description', 'release_year',
                  'language', 'rental_duration', 'rental_rate', 'length',
                  'replacement_cost', 'rating', 'last_update',
                  'special_features', 'fulltext']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(FilmForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(FilmForm, self).is_valid()

    def full_clean(self):
        return super(FilmForm, self).full_clean()

    def clean_film_id(self):
        film_id = self.cleaned_data.get("film_id", None)
        return film_id

    def clean_title(self):
        title = self.cleaned_data.get("title", None)
        return title

    def clean_description(self):
        description = self.cleaned_data.get("description", None)
        return description

    def clean_release_year(self):
        release_year = self.cleaned_data.get("release_year", None)
        return release_year

    def clean_language(self):
        language = self.cleaned_data.get("language", None)
        return language

    def clean_rental_duration(self):
        rental_duration = self.cleaned_data.get("rental_duration", None)
        return rental_duration

    def clean_rental_rate(self):
        rental_rate = self.cleaned_data.get("rental_rate", None)
        return rental_rate

    def clean_length(self):
        length = self.cleaned_data.get("length", None)
        return length

    def clean_replacement_cost(self):
        replacement_cost = self.cleaned_data.get("replacement_cost", None)
        return replacement_cost

    def clean_rating(self):
        rating = self.cleaned_data.get("rating", None)
        return rating

    def clean_last_update(self):
        last_update = self.cleaned_data.get("last_update", None)
        return last_update

    def clean_special_features(self):
        special_features = self.cleaned_data.get("special_features", None)
        return special_features

    def clean_fulltext(self):
        fulltext = self.cleaned_data.get("fulltext", None)
        return fulltext

    def clean(self):
        return super(FilmForm, self).clean()

    def validate_unique(self):
        return super(FilmForm, self).validate_unique()

    def save(self, commit=True):
        return super(FilmForm, self).save(commit)


class FilmActorForm(forms.ModelForm):
    class Meta:
        model = FilmActor
        fields = ['film_id', 'actor_id', 'last_update']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(FilmActorForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(FilmActorForm, self).is_valid()

    def full_clean(self):
        return super(FilmActorForm, self).full_clean()

    def clean_actor(self):
        actor = self.cleaned_data.get("actor_id", None)
        return actor

    def clean_film(self):
        film = self.cleaned_data.get("film_id", None)
        return film

    def clean_last_update(self):
        last_update = self.cleaned_data.get("last_update", None)
        return last_update

    def clean(self):
        return super(FilmActorForm, self).clean()

    def validate_unique(self):
        return super(FilmActorForm, self).validate_unique()

    def save(self, commit=True):
        return super(FilmActorForm, self).save(commit)


class FilmCategoryForm(forms.ModelForm):
    class Meta:
        model = FilmCategory
        fields = ['film_id', 'category_id', 'last_update']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(FilmCategoryForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(FilmCategoryForm, self).is_valid()

    def full_clean(self):
        return super(FilmCategoryForm, self).full_clean()

    def clean_film(self):
        film = self.cleaned_data.get("film", None)
        return film

    def clean_category(self):
        category = self.cleaned_data.get("category", None)
        return category

    def clean_last_update(self):
        last_update = self.cleaned_data.get("last_update", None)
        return last_update

    def clean(self):
        return super(FilmCategoryForm, self).clean()

    def validate_unique(self):
        return super(FilmCategoryForm, self).validate_unique()

    def save(self, commit=True):
        return super(FilmCategoryForm, self).save(commit)


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['inventory_id', 'film', 'store_id', 'last_update']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(InventoryForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(InventoryForm, self).is_valid()

    def full_clean(self):
        return super(InventoryForm, self).full_clean()

    def clean_inventory_id(self):
        inventory_id = self.cleaned_data.get("inventory_id", None)
        return inventory_id

    def clean_film(self):
        film = self.cleaned_data.get("film", None)
        return film

    def clean_store_id(self):
        store_id = self.cleaned_data.get("store_id", None)
        return store_id

    def clean_last_update(self):
        last_update = self.cleaned_data.get("last_update", None)
        return last_update

    def clean(self):
        return super(InventoryForm, self).clean()

    def validate_unique(self):
        return super(InventoryForm, self).validate_unique()

    def save(self, commit=True):
        return super(InventoryForm, self).save(commit)


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['language_id', 'name', 'last_update']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(LanguageForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(LanguageForm, self).is_valid()

    def full_clean(self):
        return super(LanguageForm, self).full_clean()

    def clean_language_id(self):
        language_id = self.cleaned_data.get("language_id", None)
        return language_id

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_last_update(self):
        last_update = self.cleaned_data.get("last_update", None)
        return last_update

    def clean(self):
        return super(LanguageForm, self).clean()

    def validate_unique(self):
        return super(LanguageForm, self).validate_unique()

    def save(self, commit=True):
        return super(LanguageForm, self).save(commit)


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['payment_id', 'customer', 'staff', 'rental', 'amount',
                  'payment_date']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(PaymentForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(PaymentForm, self).is_valid()

    def full_clean(self):
        return super(PaymentForm, self).full_clean()

    def clean_payment_id(self):
        payment_id = self.cleaned_data.get("payment_id", None)
        return payment_id

    def clean_customer(self):
        customer = self.cleaned_data.get("customer", None)
        return customer

    def clean_staff(self):
        staff = self.cleaned_data.get("staff", None)
        return staff

    def clean_rental(self):
        rental = self.cleaned_data.get("rental", None)
        return rental

    def clean_amount(self):
        amount = self.cleaned_data.get("amount", None)
        return amount

    def clean_payment_date(self):
        payment_date = self.cleaned_data.get("payment_date", None)
        return payment_date

    def clean(self):
        return super(PaymentForm, self).clean()

    def validate_unique(self):
        return super(PaymentForm, self).validate_unique()

    def save(self, commit=True):
        return super(PaymentForm, self).save(commit)


class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['rental_id', 'rental_date', 'inventory', 'customer',
                  'return_date', 'staff', 'last_update']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(RentalForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(RentalForm, self).is_valid()

    def full_clean(self):
        return super(RentalForm, self).full_clean()

    def clean_rental_id(self):
        rental_id = self.cleaned_data.get("rental_id", None)
        return rental_id

    def clean_rental_date(self):
        rental_date = self.cleaned_data.get("rental_date", None)
        return rental_date

    def clean_inventory(self):
        inventory = self.cleaned_data.get("inventory", None)
        return inventory

    def clean_customer(self):
        customer = self.cleaned_data.get("customer", None)
        return customer

    def clean_return_date(self):
        return_date = self.cleaned_data.get("return_date", None)
        return return_date

    def clean_staff(self):
        staff = self.cleaned_data.get("staff", None)
        return staff

    def clean_last_update(self):
        last_update = self.cleaned_data.get("last_update", None)
        return last_update

    def clean(self):
        return super(RentalForm, self).clean()

    def validate_unique(self):
        return super(RentalForm, self).validate_unique()

    def save(self, commit=True):
        return super(RentalForm, self).save(commit)


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['staff_id', 'first_name', 'last_name', 'address', 'email',
                  'store_id', 'active', 'username', 'password', 'last_update',
                  ]
        exclude = ['picture']
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(StaffForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(StaffForm, self).is_valid()

    def full_clean(self):
        return super(StaffForm, self).full_clean()

    def clean_staff_id(self):
        staff_id = self.cleaned_data.get("staff_id", None)
        return staff_id

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name", None)
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name", None)
        return last_name

    def clean_address(self):
        address = self.cleaned_data.get("address", None)
        return address

    def clean_email(self):
        email = self.cleaned_data.get("email", None)
        return email

    def clean_store_id(self):
        store_id = self.cleaned_data.get("store_id", None)
        return store_id

    def clean_active(self):
        active = self.cleaned_data.get("active", None)
        return active

    def clean_username(self):
        username = self.cleaned_data.get("username", None)
        return username

    def clean_password(self):
        password = self.cleaned_data.get("password", None)
        return password

    def clean_last_update(self):
        last_update = self.cleaned_data.get("last_update", None)
        return last_update

    def clean_picture(self):
        picture = self.cleaned_data.get("picture", None)
        return picture

    def clean(self):
        return super(StaffForm, self).clean()

    def validate_unique(self):
        return super(StaffForm, self).validate_unique()

    def save(self, commit=True):
        return super(StaffForm, self).save(commit)


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['store_id', 'manager_staff', 'address', 'last_update']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(StoreForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(StoreForm, self).is_valid()

    def full_clean(self):
        return super(StoreForm, self).full_clean()

    def clean_store_id(self):
        store_id = self.cleaned_data.get("store_id", None)
        return store_id

    def clean_manager_staff(self):
        manager_staff = self.cleaned_data.get("manager_staff", None)
        return manager_staff

    def clean_address(self):
        address = self.cleaned_data.get("address", None)
        return address

    def clean_last_update(self):
        last_update = self.cleaned_data.get("last_update", None)
        return last_update

    def clean(self):
        return super(StoreForm, self).clean()

    def validate_unique(self):
        return super(StoreForm, self).validate_unique()

    def save(self, commit=True):
        return super(StoreForm, self).save(commit)
