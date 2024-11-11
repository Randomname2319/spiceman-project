from django.urls import path
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("Y/", include("Y.urls")),
    path("admin/", admin.site.urls),
    path("",include('spiceman.urls'))
]
