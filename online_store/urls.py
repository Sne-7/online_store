from django.contrib import admin
from django.urls import path
from django.http import HttpResponse  # ✅ Required import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: HttpResponse("Welcome to the Online Store!")),  # Just a test view
]
