# Mailchimp Django integration

Class to add emails to Mailchimp lists.

## Install

```bash
pip install git+https://github.com/GeoSchool/django-mailchimp3-emailcollector.git
```

Add `mailchimp3` to your INSTALLED_APPS, then define the `MAILCHIMP_API_KEY` setting.

## Usage

```python
# Initialize the integration
mc = Mailchimp()
# Trigger the action on the given list
added = mc.add_member_to_list(settings.MAILCHIMP_LIST_ID, email)
if added:
    print("Email successfully added")
```

## Running tests

```bash
virtualenv --python=python3 env
source env/bin/activate
pip install -r requirements-test.txt
python tests.py
```

You can also run the coverage:

```bash
pip install coverage
coverage run tests.py
# Display the results
coverage report -m
```
