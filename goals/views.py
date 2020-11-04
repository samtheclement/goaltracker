from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Goal

class GoalListView(LoginRequiredMixin, ListView):
    model = Goal
    template_name = 'goal_list.html'
    login_url = 'login'

class GoalDetailView(LoginRequiredMixin, DetailView):
    model = Goal
    template_name = 'goal_detail.html'
    login_url = 'login'


class GoalUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Goal
    fields = ('title', 'body', )
    template_name = 'goal_edit.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class GoalDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Goal
    template_name = 'goal_delete.html'
    success_url = reverse_lazy('goal_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class GoalCreateView(LoginRequiredMixin, CreateView):
    model = Goal
    template_name = 'goal_new.html'
    fields = ('title', 'body',)
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
