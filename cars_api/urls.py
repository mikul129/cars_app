from django.urls import include, path,re_path
from .views import CarsCreate, CarsList, \
    CarsUpdate, CarsDelete

urlpatterns = [
    path('create/', CarsCreate.as_view(), name='create-car'),
    path('', CarsList.as_view()),
    path('update/<int:pk>/', CarsUpdate.as_view(), name='update-car'),
    path('delete/<int:pk>/', CarsDelete.as_view(), name='delete-car')
    ]