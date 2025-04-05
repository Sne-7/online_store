from django.contrib import admin
from django.urls import path
from store.views import homepage
from .views import ProductListView# ✅ Import view
from django.urls import path, include
from .views import product_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('', include('store.urls')),
]


