from django.urls import path,include
from . import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('search',views.search,name='search'),

    path('all_books',views.all_books,name='all_books'),
    path('genre/<str:slug>',views.category_detail,name='category_detail'),
    path('<str:slug>',views.book_detail,name='book_detail'),
        path('rate/<str:slug>',views.Rate,name='rate'),




]