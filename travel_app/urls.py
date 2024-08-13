# destinations/urls.py
from django.urls import path
from .views import (
    DestinationListCreate, destination_list, destination_detail,
    destination_update, destination_delete,dest_index
)

urlpatterns = [
    path('api/destinations/', DestinationListCreate.as_view(), name='destination-api-list-create'),
    path('', dest_index, name='destination-list'),
    path('create/', destination_list, name='create'),
    path('<int:pk>/', destination_detail, name='destination-detail'),
    path('<int:pk>/update/', destination_update, name='destination-update'),
    path('<int:pk>/delete/', destination_delete, name='destination-delete'),
]
