from django.urls import path
from courses.views import courses_view_detail, courses_view_list,courses_view_create,courses_view_delete, courses_view_update
# app_name = 'course'
urlpatterns=[
    path('',courses_view_list.as_view(),name='courses-view-list'),
    path('create/',courses_view_create.as_view(),name='courses-view-create'),
    path('<int:id>',courses_view_detail.as_view(),name='courses-view-details'),
    path('<int:id>/delete',courses_view_delete.as_view(),name='courses-view-delete'),
    path('<int:id>/update',courses_view_update.as_view(),name='courses-view-update'),
]