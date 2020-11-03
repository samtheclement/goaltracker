from django.urls import path
from .views import (
    GoalListView,
    GoalUpdateView,
    GoalDetailView,
    GoalDeleteView,
)

urlpatterns = [
    path('<int:pk>/edit/', GoalUpdateView.as_view(), name='goal_edit'),
    path('<int:pk>/', GoalDetailView.as_view(), name='goal_detail'),
    path('<int:pk>/delete/', GoalDeleteView.as_view(), name='goal_delete'),
    path('',GoalListView.as_view(), name='goal_list'),
]
