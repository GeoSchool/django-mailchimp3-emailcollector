from django.apps import AppConfig


class MCAppConfig(AppConfig):

    name = 'mailchimp3'
    verbose_name = 'Mailchimp integration'

    def ready(self):
        from . import checks
