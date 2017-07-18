# Mailchimp Django integration

Class to add emails to Mailchimp lists.

## Install

```bash
pip install git+https://github.com/GeoSchool/django-mailchimp3-emailcollector.git
```

## Usage

```python
# Initialize the integration
mc = Mailchimp(settings.MAILCHIMP_API_KEY)
# Trigger the action on the given list
added = mc.add_member_to_list(settings.MAILCHIMP_LIST_ID, email)
if added:
    print("Email successfully added")
```
