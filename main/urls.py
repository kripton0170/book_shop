from django.urls import path
from .views import MainView, CreateBookView, UpdateBookView, DetailBookView, DeleteBookView

urlpatterns = [
    path('', MainView.as_view(), name="home"),
    path('create/', CreateBookView.as_view(), name="create"),
    path('update/<int:pk>/', UpdateBookView.as_view(), name="update"),
    path('detail/<int:pk>/', DetailBookView.as_view(), name="detail"),
    path('delete/<int:pk>/', DeleteBookView.as_view(), name="delete"),
]