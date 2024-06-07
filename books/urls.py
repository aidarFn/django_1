from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books_list),
    path('books/<int:id>/', views.books_detail_view),

    path('name/', views.name_view),
    path('hobby/', views.hobby_view),
    path('time/', views.times_view),
    path('random/', views.random_view)
]