from django.urls import path

from users.apps import UsersConfig
from users.views import user_login_view, user_logout_view, UserUpdateView, UserPasswordChangeView, UserProfileView, \
    UserListView, AllUserProfileView, ALLUserUpdateView, UserDeleteView, UserCreateView

app_name = UsersConfig.name

urlpatterns = [
    path('', user_login_view, name="login_user"), #  url стартовой страницы для входа
    path('logout/', user_logout_view, name="logout_user"), # выход пользователя
    path('profile/', UserProfileView.as_view(), name='profile_user'), # страница профиля авторизированного пользователя
    path('update/', UserUpdateView.as_view(), name="update_user"), # редактирование данных авторизированного пользователя
    path('change_password/', UserPasswordChangeView.as_view(), name='change_password_user'), # смена пароля авторизированного пользователя

# просмотр других пользователей
    path('all_users/', UserListView.as_view(), name='users_list'), # просмотр всех пользователей
    path('create/', UserCreateView.as_view(), name='create_user'), # создание пользователя
    path('profile/<int:pk>/', AllUserProfileView.as_view(), name='profile_all_user'), # просмотр профиля пользователя
    path('update/<int:pk>/', ALLUserUpdateView.as_view(), name='update_all_user'), # редактирование профиля пользователя
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='delete_user'), # удаление пользователя
]
