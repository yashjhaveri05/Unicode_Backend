from django.urls import path
from . import views

app_name = 'weather'

urlpatterns = [
    path('task/<int:x>/<int:y>', views.task, name="task1"), 
    path('',views.index, name="index"),
    path('delete/<city_name>/', views.delete_city, name='delete_city'),
    path('github/',views.github, name="github"),
    path('user_search/', views.user_search, name="user_search"),
    path('view_weather/', views.view_weather, name="view_weather"),
    path('top_three/', views.top_three, name="top_three"),
    path('search/', views.weather_search, name="search"), 
]
