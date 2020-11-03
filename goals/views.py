from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Goal

class GoalListView(ListView):
    model = Goal
    template_name = 'goal_list.html'

class GoalDetailView(DetailView):
    model = Goal
    template_name = 'goal_detail.html'

class GoalUpdateView(UpdateView):
    model = Goal
    fields = ('title', 'body', )
    template_name = 'goal_edit.html'

class GoalDeleteView(DeleteView):
    model = Goal
    template_name = 'goal_delete.html'
    success_url = reverse_lazy('goal_list')

class GoalCreateView(CreateView):
    model = Goal
    template_name = 'article_new.html'
    fields = ('title', 'body', 'author',)
