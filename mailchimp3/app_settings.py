from django.conf import settings

# The API key needed to access the service
MAILCHIMP_API_KEY = getattr(settings, 'MAILCHIMP_API_KEY', '')
