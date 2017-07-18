from django.conf import settings

# The API key needed to access the service
MAILCHIMP_API_KEY = getattr(settings, 'MAILCHIMP_API_KEY', '')

MAILCHIMP_API_URL = getattr(
    settings,
    'MAILCHIMP_API_URL',
    'https://{datacenter}.api.mailchimp.com/3.0/',
)
