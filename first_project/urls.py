"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from product.views import welcome, plain_text_view, html_view, greet_user, hello_template_view, users_list_view, get_products, create_product, hard_delete_product, update_product, soft_delete_product, upload_csv, download_csv


urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", welcome),
    path("ptv/", plain_text_view),
    path("html-view/", html_view),
    path("greet-user/", greet_user),
    path("htv/", hello_template_view),
    path("ulv/", users_list_view),
    path("products/", get_products, name="get_all_products"),
    path("create-product/", create_product, name="create_prod"),
    path("hard-delete-product/<int:pid>/", hard_delete_product, name="hard_delete_prod"),
    path("soft-delete-product/<int:pid>/", soft_delete_product, name="soft_delete_prod"),
    path("update-product/<int:pid>/", update_product, name="update_prod"),

    path("upload-csv/", upload_csv, name="upload_csv"),
    path("download-csv/", download_csv, name="download_csv"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls"))


]

# http://127.0.0.1:8000/delete-product/1
