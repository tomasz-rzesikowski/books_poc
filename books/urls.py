from django.urls import path

from books import views

app_name = 'books'

urlpatterns = [
    path('', views.ListBookView.as_view(), name='list-books'),
    path('create', views.CreateBookView.as_view(), name='create-book')
]
