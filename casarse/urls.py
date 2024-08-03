
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ap_principal.urls')),  # Incluye las URLs de ap_principal
]
