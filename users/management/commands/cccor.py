# cleanup_old_records
from django.core.management.base import BaseCommand
from django.utils import timezone

from datetime import timedelta, datetime

from users.models import Action


class Command(BaseCommand):
    """Команда удаления записей действий пользователй"""
    help = 'Удаляет записи старше 30 дней'

    def handle(self, *args, **kwargs):
        # Определяем дату, старше которой записи будут удалены
        cutoff_date = timezone.now() - timedelta(days=180)

        # Удаляем записи
        deleted_count, _ = Action.objects.filter(date__lt=cutoff_date).delete()

        self.stdout.write(self.style.SUCCESS(f'Удалено {deleted_count} записей'))
