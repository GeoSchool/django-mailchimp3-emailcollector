from django.core.checks import Error, register

from . import app_settings


@register()
def config_settings_present(app_configs, **kwargs):
    """
    Check that the configuration is present
    """

    # This check is only relevant for this app
    if app_configs and 'mailchimp3' not in app_configs:
        # A list if apps has been provided but we are not part of it
        return []

    errors = []

    for config_key in ['MAILCHIMP_API_KEY']:
        if getattr(app_settings, config_key, '') == '':
            errors.append(
                Error(
                    "The setting {} is not defined and is required by the Mailchimp3 integration.".
                    format(config_key),
                    hint='Please define a value for {} in your settings file.'.
                    format(config_key),
                    obj=config_key,
                    id='mailchimp3.E001',
                )
            )

    if len(app_settings.MAILCHIMP_API_KEY) < 35 or \
            app_settings.MAILCHIMP_API_KEY.find('-') == -1:
        errors.append(
            Error(
                "Mailchimp Api Key should be at least 35 characters"
                " and contain a dash."
            )
        )

    return errors
