from django.contrib import admin
from django.urls import path, include
from escola import views

urlpatterns = [
    path('', include('escola.urls')),
    path('admin/', admin.site.urls),
]
