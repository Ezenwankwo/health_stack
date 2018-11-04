from django.urls import path

from . import views


urlpatterns = [
    path('folder/create/', views.FolderCreateView.as_view(), name='create_folder'),
    path('folder/update/<slug>/', views.FolderUpdateView.as_view(), name='update_folder'),
    path('folder/list/', views.FolderListView.as_view(), name='list_folder'),
    path('folder/detail/<slug>/', views.FolderDetailView.as_view(), name='detail_folder'),
    path('folder/delete/<slug>/', views.FolderDeleteView.as_view(), name='delete_folder'),

    path('file/upload/', views.FileUploadView.as_view(), name='upload_file'),
    path('file/update/<slug>/', views.FileUpdateView.as_view(), name='update_file'),
    path('file/list/', views.FileListView.as_view(), name='list_file'),
    path('file/delete/<slug>/', views.FileDeleteView.as_view(), name='delete_file'),
]
