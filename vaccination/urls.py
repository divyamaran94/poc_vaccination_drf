from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vaccination_api.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
