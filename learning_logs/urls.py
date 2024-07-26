from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    path('', views.all_topics, name='all_topics'),
    path('add_all', views.index, name='index'),
    path('add_topic/', views.index, name='add_topic'),
    path('<str:topic_name>/', views.add_entry, name='add_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('topic/<str:topic_name>/', views.topic, name='topic'),
]
