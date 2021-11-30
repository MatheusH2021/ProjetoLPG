from django.urls import path, include

from . import views

app_name = 'places'

urlpatterns = [
    path('', views.home, name='home'),
    path('places/', views.places, name='places'),
    path('newplace/', views.newPlace, name="new-place"),
    path('manage/', views.manage, name="manage"),
    path("<slug:slug>/", views.PlaceDetailView.as_view(), name="detail"),
    path('edit/<int:id>/', views.editPlace, name="edit-place"),
    path('delete/<int:id>/', views.deletePlace, name="delete-place"),       
]