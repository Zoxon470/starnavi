import clearbit
from django.conf import settings
from django.db import transaction
from django_rq import job
from pyhunter import PyHunter
from requests.exceptions import HTTPError


@job
def verify_email(user):
    hunter = PyHunter(settings.HUNTER_KEY)
    response = hunter.email_verifier(user.email)
    if response['regexp'] and response['smtp_check']:
        user.verified_email = True
        user.save(update_fields=['verified_email'])


@job
def find_enrichment(user):
    with transaction.atomic():
        clearbit.key = settings.CLEARBIT_KEY
        try:
            response = clearbit.Enrichment.find(email=user.email, stream=True)
        except HTTPError:
            pass
        try:
            user.first_name = response['person']['name']['givenName'],
            user.last_name = response['person']['name']['familyName']
            user.save(update_fields=['first_name', 'last_name'])
        except TypeError:
            pass
