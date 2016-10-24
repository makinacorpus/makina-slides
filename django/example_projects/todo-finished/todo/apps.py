from django.apps import AppConfig


class TodoConfig(AppConfig):
    name = 'todo'

    def ready(self):
        import signals  # NOQA
