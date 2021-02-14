from django.shortcuts import render, get_object_or_404
from django.views.generic import (
     ListView,
     CreateView,
     DetailView,
     UpdateView,
     DeleteView
)
from .models import GoalForDays,Day
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .forms import GoalForm
from django.views.generic.edit import FormMixin

def goals_main(request):
    data = {
        'title': 'Ваши цели'
    }
    return render(request,'plan/plan-main.html',data)


class ShowDays(ListView):
    model = Day
    template_name = 'plan/plan-day.html'
    context_object_name = 'goal_day'
    ordering = ['-date']

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Day.objects.filter(author=user).order_by('-date')


    def get_context_data(self, **kwards):
        ctx = super(ShowDays,self).get_context_data(**kwards)

        ctx['title'] = 'Цели на день'
        return ctx


class CreateDays(LoginRequiredMixin,CreateView):
    model = Day
    template_name = 'plan/day-add.html'

    fields = ['date']

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Day.objects.filter(author=user)


    def get_context_data(self, **kwards):
        ctx = super(CreateDays, self).get_context_data(**kwards)

        ctx['title'] = 'Добавление дня '
        ctx['btn_text'] = 'Добавить день'
        return ctx

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DayDetailView(DetailView,FormMixin):
    model = Day
    template_name = 'plan/day-detail.html'
    form_class = GoalForm
    # def get_queryset(self):
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))
    #     return Day.objects.filter(author=user)

    def get_context_data(self, **kwards):
        ctx = super(DayDetailView,self).get_context_data(**kwards)
        day = Day.objects.filter(pk=self.kwargs['pk']).first()

        ctx['title'] = Day.objects.get(pk=self.kwargs['pk']).date
        ctx['goals'] = GoalForDays.objects.filter(date=day)
        #Переменная для подставления порядкового номера при выводе
        x = len(ctx['goals'])
        count_goals = []
        for n in range(x):
            count_goals.append(n+1)

        ctx['count'] = count_goals
        ctx['form'] = GoalForm()
        return ctx


    def get_success_url(self):
        a = str(self.kwargs['pk'])
        url = 'day-' + self.kwargs['username'] + '/' + a
        return '/plan/' + url



    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        day = Day.objects.filter(pk=self.kwargs['pk']).first()
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.date = day
        print(self.object.author)
        print(self.object.date)
        self.object.save()
        return super().form_valid(form)

class DayGoalDeleteView(LoginRequiredMixin,DeleteView,UserPassesTestMixin):

    def get_context_data(self, **kwards):
        day = Day.objects.filter(pk=self.kwargs['pk']).first()

    def get_success_url(self):
        day = Day.objects.filter(pk=self.kwargs['pk']).first()
        a = str(self.kwargs['pk'])
        url = 'day-' + self.kwargs['username']
        return '/plan/' + url

    model = GoalForDays
    # success_url = 'day-detail'
    template_name = 'plan/plan-day-delete.html'

    def test_func(self):
        goal = self.get_object()
        if self.request.user  == goal.author:
            return True

        return False