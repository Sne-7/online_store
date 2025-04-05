from django.contrib import admin
from django.urls import path
from store.views import homepage  # ✅ Import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),  # ✅ Use the homepage view
]
