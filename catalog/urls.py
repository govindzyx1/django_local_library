from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),path('books/', views.BookListView.as_view(), name='books'),

    path('book/<int:pk>', views.book_detail_view, name='book-detail'),
]
urlpatterns += [   
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]
urlpatterns += [   
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]
urlpatterns += [   
    path('send', views.subscribe, name='subscribe'),
]
