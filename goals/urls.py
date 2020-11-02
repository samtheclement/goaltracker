from django.urls import path
from .views import ArticleListView
urlpatterns = [
    path('',GoalListView.as_view(), name='goal_list')
]
