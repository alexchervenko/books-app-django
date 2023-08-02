from django.urls import path

from reviews import views

urlpatterns = [
    path('', views.index, name='welcome_view'),
    path('books/', views.book_list, name='book_list'),
]