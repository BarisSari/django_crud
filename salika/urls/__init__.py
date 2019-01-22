from django.conf.urls import include, url

app_name="salika"

urlpatterns = [

    url(r'^actors/', include('salika.urls.actor_urls')),  # NOQA
    url(r'^addresss/', include('salika.urls.address_urls')),
    url(r'^auth_groups/', include('salika.urls.auth_group_urls')),
    url(r'^auth_group_permissionss/', include('salika.urls.auth_group_permissions_urls')),
    url(r'^auth_permissions/', include('salika.urls.auth_permission_urls')),
    url(r'^auth_users/', include('salika.urls.auth_user_urls')),
    url(r'^auth_user_groupss/', include('salika.urls.auth_user_groups_urls')),
    url(r'^auth_user_user_permissionss/', include('salika.urls.auth_user_user_permissions_urls')),
    url(r'^categorys/', include('salika.urls.category_urls')),
    url(r'^citys/', include('salika.urls.city_urls')),
    url(r'^countrys/', include('salika.urls.country_urls')),
    url(r'^customers/', include('salika.urls.customer_urls')),
    url(r'^django_admin_logs/', include('salika.urls.django_admin_log_urls')),
    url(r'^django_content_types/', include('salika.urls.django_content_type_urls')),
    url(r'^django_migrationss/', include('salika.urls.django_migrations_urls')),
    url(r'^django_sessions/', include('salika.urls.django_session_urls')),
    url(r'^films/', include('salika.urls.film_urls')),
    url(r'^film_actors/', include('salika.urls.film_actor_urls')),
    url(r'^film_categorys/', include('salika.urls.film_category_urls')),
    url(r'^inventorys/', include('salika.urls.inventory_urls')),
    url(r'^languages/', include('salika.urls.language_urls')),
    url(r'^payments/', include('salika.urls.payment_urls')),
    url(r'^rentals/', include('salika.urls.rental_urls')),
    url(r'^staffs/', include('salika.urls.staff_urls')),
    url(r'^stores/', include('salika.urls.store_urls')),
]
