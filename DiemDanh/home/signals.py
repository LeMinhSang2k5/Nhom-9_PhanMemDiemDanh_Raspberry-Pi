from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_groups(sender, **kwargs):
    if sender.name == "history_attendance": 
        Group.objects.get_or_create(name='Teachers')
        Group.objects.get_or_create(name='Students')
