
from django.contrib import admin
from django.urls import path
from pagination import views
from pagination.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagination, name="pagination")
]
