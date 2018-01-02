from django.apps import AppConfig


class SmstorConfig(AppConfig):
    name = 'smstor'

    def ready(self):
        import smstor.signals
