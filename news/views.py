from datetime import datetime

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from news.forms import ArticleForm
from news.models import Article
from users.action import journal_user_action


class NewsListView(ListView):
    """Список всех статей"""
    model = Article
    paginate_by = 5
    queryset = Article.objects.order_by('-date')
    template_name = 'news/news_list.html'
    extra_context = {
        'title': f'Новости'
    }


class ArticleDetailView(DetailView):
    """ Детальный просмотр статьи"""
    model = Article
    template_name = 'news/news_detail.html'

    def get_context_data(self, **kwargs):
        contex_data = super().get_context_data(**kwargs)
        contex_data['title'] = f'{self.object.title}'
        return contex_data


class ArticleCreateView(CreateView):
    """ Создание новой статьи"""
    model = Article
    form_class = ArticleForm
    success_url = reverse_lazy('news:news_list')
    template_name = 'news/news_create.html'
    extra_context = {
        'title': f'Добавление статьи'
    }

    def form_valid(self, form):
        form.instance.date = datetime.now()  # assuming you want the current login user to be set to the user
        self.object = form.save()  # сохраняем созданный объект
        journal_user_action(self.request.user, f"Создание статьи {self.object.title}")
        return super(ArticleCreateView, self).form_valid(form)


class ArticleUpdateView(UpdateView):
    """ Редактирование статьи"""
    model = Article
    form_class = ArticleForm
    template_name = 'news/news_create.html'
    success_url = reverse_lazy('news:news_list')

    def get_context_data(self, **kwargs):
        contex_data = super().get_context_data(**kwargs)
        if self.object:
            # если объект есть, тогда вписываем первый
            article_name = self.object.title
            contex_data['title'] = f'Редактирование статьи {article_name}'
        else:
            contex_data['title'] = f'Нет статьи'
        journal_user_action(self.request.user, f"Редактирование статьи {self.object.title}")
        return contex_data


class ArticleDeleteView(PermissionRequiredMixin, DeleteView):
    """ Удаление статьи"""
    model = Article
    template_name = 'news/news_delete.html'
    success_url = reverse_lazy('news:news_list')
    permission_required = 'news.delete_news'
    extra_context = {
        'title': f'Удаление статьи'
    }
    def form_valid(self, form):
        # Вызываем метод для записи действия пользователя через form_valid
        journal_user_action(self.request.user, f"Удаление статьи {self.object.title}")
        return super().form_valid(form)
