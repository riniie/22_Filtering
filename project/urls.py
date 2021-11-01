from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import StudentList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest/', include('rest_framework.urls')),
    path('student/', StudentList.as_view(), name='student-list'),
]
