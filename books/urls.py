from django.urls import path

from books import views

app_name = 'books'

urlpatterns = [
    path('', views.ListBookView.as_view(), name='list-books'),
    path('create/', views.CreateBookView.as_view(), name='create-book'),
    path('<int:pk>/', views.UpdateBookView.as_view(), name='update-book'),
    path('create_author/', views.CreateAuthorView.as_view(), name='create-author'),
    path('create_pub_lang/', views.CreateLanguageView.as_view(), name='create-pub-lang'),
    path('import_books/', views.ListImportView.as_view(), name='list-import-books'),
]
