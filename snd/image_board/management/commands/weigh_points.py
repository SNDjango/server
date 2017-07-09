from django.core.management.base import BaseCommand, CommandError
from image_board.models import ContentItem
import datetime

class Command(BaseCommand):
    def handle(self, *args, **options):
        now = datetime.datetime.now().replace(tzinfo=None)

        all_posts = ContentItem.objects.all()

        for post in all_posts:
            delta_m = (now - post.upload_date.replace(tzinfo=None)).total_seconds() / 60
            self.stdout.write(self.style.SUCCESS('delta_m "%d"' % delta_m))
            post.points_weighted = post.points - (post.points * (delta_m * 0.001))
            post.save()
