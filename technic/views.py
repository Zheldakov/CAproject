from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import reverse
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView

from technic.forms import DepartmentForm, TypeTechnicForm, TechnicForm
from technic.models import Technic, TypeTechnic, Department


class TechnicListView(ListView):
    """ Список всей техники."""
    model = Technic
    paginate_by = 6
    template_name = 'technic/technic_list.html'
    extra_context = {
        'title': f'Техника'
    }

class TechnicCreateView(CreateView):
    """ Создание техники"""
    model = Technic
    form_class = TechnicForm
    success_url = reverse_lazy('technic:technic_list')
    template_name = 'technic/technic_create.html'
    extra_context = {
        'title': f'Добавление техники'
    }


class TechnicDetailView(DetailView):
    """ Просмотр детальной информации по техники."""
    model = Technic
    template_name = 'technic/technic_detail.html'
    extra_context = {
        'title': f'Детальная информация'
    }

class TechnicUpdateView(UpdateView):
    """ Изменение техники."""
    model = Technic
    form_class = TechnicForm
    template_name = 'technic/Technic_update.html'
    extra_context = {
        'title': f'Редактирование техники'
    }
    def get_success_url(self):
        # Переходим на страницу детальной информации по технике после редактирования
        return reverse('technic:technic_detail', args=[self.kwargs.get('pk')])

class TechnicDeleteView(PermissionRequiredMixin, DeleteView):
    """ Страница удаления техники."""
    model = Technic
    template_name = 'technic/technic_delete.html'
    success_url = reverse_lazy('technic:technic_list')
    permission_required = 'technic.delete_technic'
    extra_context = {
        'title': f'Удаление техники'
    }

class DepartmentListView(ListView):
    """ Показывает страницу с информацией о техники определенного подразделения"""
    model = Department
    template_name = 'technic/dep_list.html'
    extra_context = {
        'title': f'Подразделения'
    }


class TypeListView(ListView):
    """ Показывает страницу с информацией о техники определенного типа"""
    model = TypeTechnic
    template_name = 'technic/type_list.html'
    extra_context = {
        'title': f'Типы техники'
    }


class DepartmentCreateView(CreateView):
    """ Создание подразделения"""
    model = Department
    form_class = DepartmentForm
    success_url = reverse_lazy('technic:department_list')
    template_name = 'technic/dep_create.html'
    extra_context = {
        'title': f'Создание подразделения'
    }


class DepartmentUpdateView(UpdateView):
    """ Изменение подразделения"""
    model = Department
    form_class = DepartmentForm
    template_name = 'technic/dep_update.html'
    success_url = reverse_lazy('technic:department_list')
    extra_context = {
        'title': f'Редактирование подразделения'
    }


class DepartmentDeleteView(PermissionRequiredMixin, DeleteView):
    """ Страница удаления подразделения."""
    model = Department
    template_name = 'technic/dep_delete.html'
    success_url = reverse_lazy('technic:department_list')
    permission_required = 'technic.delete_department'
    extra_context = {
        'title': f'Удаление подразделения'
    }


class TypeTechnicCreateView(CreateView):
    """ Создание типа техники"""
    model = TypeTechnic
    form_class = TypeTechnicForm
    success_url = reverse_lazy('technic:type_list')
    template_name = 'technic/type_create.html'
    extra_context = {
        'title': f'Создание типа техники'
    }


class TypeTechnicUpdateView(UpdateView):
    """ Изменение типа техники."""
    model = TypeTechnic
    form_class = TypeTechnicForm
    template_name = 'technic/type_update.html'
    success_url = reverse_lazy('technic:type_list')
    extra_context = {
        'title': f'Редактирование подразделения'
    }


class TypeTechnicDeleteView(PermissionRequiredMixin, DeleteView):
    """ Страница удаления типа пользователя."""
    model = TypeTechnic
    template_name = 'technic/type_delete.html'
    success_url = reverse_lazy('technic:type_list')
    permission_required = 'technic.delete_typetechnic'
    extra_context = {
        'title': f'Удаление типа техники'
    }

# class DepartmentListFilterView(ListView):
#     """ Показывает страницу с информацией о техники определенного подразделения (для фильтрации)"""
#     model = Department
#     template_name = 'technic/dep_f_list.html'
#     extra_context = {
#         'title': f'Подразделения'
#     }
#
# class TypeListFilterView(ListView):
#     """ Показывает страницу с информацией о техники определенного типа (для фильтрации)"""
#     model = TypeTechnic
#     template_name = 'technic/type_f_list.html'
#     extra_context = {
#         'title': f'Типы техники'
#     }