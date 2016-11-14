from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from todo.models import Task


@receiver(post_save, sender=Task)
def notify_task_completion(sender, instance, created, **kwargs):
    if instance.done:
        send_mail(
            'Task "{0}" completed!'.format(instance.name),
            "Yes, it's done",
            "from@example.com",
            ["to@example.com"],
        )
