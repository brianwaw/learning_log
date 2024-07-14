from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('all_topics/', views.all_topics, name='all_topics'),
    path('<str:topic_name>/', views.add_entry, name='add_entry'),
]
