from django.urls import path
from .views import (
    GoalListView,
    GoalUpdateView,
    GoalDetailView,
    GoalDeleteView,
    GoalCreateView,
)

urlpatterns = [
    path('<int:pk>/edit/', GoalUpdateView.as_view(), name='goal_edit'),
    path('<int:pk>/', GoalDetailView.as_view(), name='goal_detail'),
    path('<int:pk>/delete/', GoalDeleteView.as_view(), name='goal_delete'),
    path('new/', GoalCreateView.as_view(), name='goal_new'),
    path('',GoalListView.as_view(), name='goal_list'),
]
