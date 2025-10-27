from django.contrib import admin
from django.urls import path
from bookapp.views import book_cover

urlpatterns = [
    path('', book_cover, name='book-cover'),
    path('admin/', admin.site.urls),
    path('book/', book_cover),
]
