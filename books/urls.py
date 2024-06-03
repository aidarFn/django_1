from django.urls import path
from books import views

urlpatterns = [
    path('name/', views.name_view),
    path('hobby/', views.hobby_view),
    path('time/', views.times_view),
    path('random/', views.random_view)
]