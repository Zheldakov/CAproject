from datetime import timedelta

from django.utils import timezone

from users.models import Action


def journal_user_action(user, action):
    action = Action(user=user, action=action)
    # Определяем дату, старше которой записи будут удалены
    action.save()
    # Удаления записей которым больше 360 дней
    cutoff_date = timezone.now() - timedelta(days=360)
    deleted_count, _ = Action.objects.filter(date__lt=cutoff_date).delete()