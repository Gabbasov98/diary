from django.shortcuts import render
from django.views.generic import (
     ListView,
     CreateView,
     DetailView,
     UpdateView,
     DeleteView
)
from .models import Biography
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

def home(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request,'biography/home.html',data)


class ShowDailyView(ListView):
    model = Biography
    template_name = 'biography/diary.html'
    context_object_name = 'biography'
    ordering = ['-date']
    paginate_by = 5

    def get_context_data(self, **kwards):
        ctx = super(ShowDailyView,self).get_context_data(**kwards)

        ctx['title'] = 'Дневник'
        return ctx


class DailyDetailView(LoginRequiredMixin,DetailView,UserPassesTestMixin):
    model = Biography
    template_name = 'biography/diary-detail.html'




    def get_context_data(self, **kwards):
        ctx = super(DailyDetailView,self).get_context_data(**kwards)

        ctx['title'] = Biography.objects.get(pk=self.kwargs['pk']).title
        return ctx



class CreateDailyView(LoginRequiredMixin,CreateView):
    model = Biography
    template_name = 'biography/diary-add.html'

    fields = ['title','text']

    def get_context_data(self, **kwards):
        ctx = super(CreateDailyView, self).get_context_data(**kwards)

        ctx['title'] = 'Добавление статьи'
        ctx['btn_text'] = 'Добавить статью'
        return ctx

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdateDailyView(LoginRequiredMixin,UpdateView,UserPassesTestMixin):
    model = Biography
    template_name = 'biography/diary-add.html'

    fields = ['title', 'text']

    def get_context_data(self, **kwards):
        ctx = super(UpdateDailyView, self).get_context_data(**kwards)

        ctx['title'] = 'Обновление статьи'
        ctx['btn_text'] = 'Обновить статью'
        return ctx


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        diary = self.get_object()
        if self.request.user  == diary.author:
            return True

        return False

class DeleteDiaryView(LoginRequiredMixin,DeleteView,UserPassesTestMixin):
    model = Biography
    success_url = '/'
    template_name = 'biography/diary-delete.html'

    def test_func(self):
        diary = self.get_object()
        if self.request.user  == diary.author:
            return True

        return False