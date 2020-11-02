from django.views.generic import ListView
from .models import Goal

class GoalListView(ListView):
    model = Article
    template_name = 'article_list.html'
