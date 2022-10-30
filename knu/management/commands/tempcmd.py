from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Temp to check if folder structure is fine'

    def handle(self, *args, **options):
        print('Command found')