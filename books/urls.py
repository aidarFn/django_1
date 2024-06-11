from django.urls import path
from . import views

urlpatterns = [
    path('all_genre/', views.all_genre),
    path('horror/', views.horror_tags_view),
    path('drama/', views.drama_tags_view),
    path('fantasy/', views.fantasy_tags_view),
    path('comedy/', views.comedy_tags_view),
    path('romance/', views.romance_tags_view),


    path('books/', views.books_list),
    path('books/<int:id>/', views.books_detail_view),

    path('name/', views.name_view),
    path('hobby/', views.hobby_view),
    path('time/', views.times_view),
    path('random/', views.random_view)
]