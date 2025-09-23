from django.urls import path
from .views import BloglistView 

urlpatterns = [
    path('', BloglistView.as_view(), name='home'),
    path('home.html', BloglistView.as_view(), name='home'),
    path('notes.html', BloglistView.as_view(), name='notes'),
]