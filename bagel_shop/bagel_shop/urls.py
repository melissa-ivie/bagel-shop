from django.contrib import admin
from django.urls import include, path

# All URLs except for /admin/ are passed on to the bagel_site app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bagel_site.urls')),
]