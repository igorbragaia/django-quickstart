from django.contrib import admin
from django.urls import path
from .views import (
    course_detail_view,
    course_create_view,
    course_delete_view,
    course_list_view,
)

app_name = 'courses'
urlpatterns = [
    path('', course_list_view, name='course-list'),
    path('create/', course_create_view, name='course-create'),
    path('<int:id>/', course_detail_view, name='course-detail'),
    path('<int:id>/delete/', course_delete_view, name='course-delete'),
]
