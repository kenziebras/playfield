from django.urls import path
from main.views import (
    show_main, create_product, show_product, show_xml, show_json, 
    show_xml_by_id, show_json_by_id, register, login_user, logout_user, 
    edit_product, delete_product, create_product_ajax, get_product_json,
    edit_product_ajax, delete_product_ajax, register_ajax, login_ajax
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('product/<str:id>/', show_product, name='show_product'), # Untuk detail page (jika masih perlu)

    # URL untuk render halaman form (bisa dihapus jika tidak dipakai)
    path('create-product-page/', create_product, name='create_product'),
    path('product/<uuid:id>/edit-page', edit_product, name='edit_product'),

    # Endpoint data JSON
    path("xml/", show_xml, name="show_xml"),
    path("json/", show_json, name="show_json"),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),

    # Endpoint AJAX untuk CRUD
    path('create-product-ajax/', create_product_ajax, name='create_product_ajax'),
    path('get-product-json/<uuid:id>/', get_product_json, name='get_product_json'),
    path('edit-product-ajax/<uuid:id>/', edit_product_ajax, name='edit_product_ajax'),
    path('delete-product-ajax/<uuid:id>/', delete_product_ajax, name='delete_product_ajax'),

    # Halaman dan Endpoint AJAX untuk Auth
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register-ajax/', register_ajax, name='register_ajax'),
    path('login-ajax/', login_ajax, name='login_ajax'),
]