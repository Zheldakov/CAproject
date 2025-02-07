from django.contrib import admin
from users.models import User, Action


# Модель User в административной панели Django
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """ Отображение в админ панели пользователей """
    list_display = ('id','role','email','first_name','last_name','phone','telegram', 'is_active') # Показываем поля в списке модели
    list_filter = ('id','email','role',) # Фильтрация
    ordering = ('id',)

@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ('id','user','action','date')