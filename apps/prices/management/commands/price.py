# 채소 가격 크롤링 하는 커스터 Django 커맨드
from django.core.management import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Get vegetable price from Crawling'

    def add_arguments(self, parser):
        parser.add_argument(
            '--name', nargs='+',
            type=str, default='cucumber'
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS(
            'Successfully get vegetable price.'))
