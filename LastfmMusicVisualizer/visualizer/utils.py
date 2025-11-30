from datetime import timedelta
from django.utils import timezone

def is_older_than(dt, hours=1):
    return (timezone.now() - dt) > timedelta(hours=hours)
