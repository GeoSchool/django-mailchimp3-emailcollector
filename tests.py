import sys

import django
from django.conf import settings

settings.configure(
    DEBUG=True,
    DATABASES={'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }},
    INSTALLED_APPS=(
        'django.contrib.auth', 'django.contrib.contenttypes',
        'django.contrib.sessions', 'django.contrib.admin', 'mailchimp3',
    )
)

if __name__ == '__main__':
    django.setup()
    from django.test.runner import DiscoverRunner
    test_runner = DiscoverRunner(verbosity=1)

    failures = test_runner.run_tests(['mailchimp3'])
    if failures:
        sys.exit(failures)