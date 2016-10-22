from django.core.management.base import BaseCommand
from todo.models import Task


class Command(BaseCommand):
    help = "Delete done tasks since 7 days"

    def handle(self, *args, **options):

        import pdb; pdb.set_trace()

        old_tasks = Task.objects.get_old()

        if old_tasks:
            old_tasks_names = old_tasks.values_list('name', flat=True)
            self.stdout.write('Tasks that will be deleted :')
            self.stdout.write(', '.join(old_tasks_names))
            old_tasks.delete()
        else:
            self.stdout.write('No task')
