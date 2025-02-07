# cleanup_old_records
from django.core.management.base import BaseCommand
from django.utils import timezone

from datetime import timedelta, datetime

from users.models import Action


class Command(BaseCommand):
    """Команда удаления записей действий пользователй"""
    help = 'Удаляет записи старше указанного количества дней'

    def add_arguments(self, parser):
        parser.add_argument(
            '--days',
            type=int,
            default=360,
            help='Количество дней, после которых записи считаются устаревшими (по умолчанию 360)',
        )

    def handle(self, *args, **kwargs):
        # Определяем дату, старше которой записи будут удалены
        days = kwargs['days']
        cutoff_date = timezone.now() - timedelta(days=days)
        old_actions = Action.objects.filter(date__lt=cutoff_date)
        if old_actions.exists():
            deleted_count, _ = old_actions.delete()
            message = f'Удалено {deleted_count} записей старше {days} дней'
            self.stdout.write(self.style.SUCCESS(message))
        else:
            message = f'Нет записей старше {days} дней для удаления.'
            self.stdout.write(self.style.WARNING(message))
