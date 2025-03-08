from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("employee/", include("employee.urls", namespace="employee")),
    path("tracker/", include("tracker.urls", namespace="tracker")),
]
