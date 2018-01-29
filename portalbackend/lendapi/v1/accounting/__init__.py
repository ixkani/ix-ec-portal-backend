import requests
from django.conf import settings

from portalbackend.lendapi.v1.accounting.models import OAuth2Config


def get_discovery_document():
    r = requests.get(settings.DISCOVERY_DOCUMENT)
    if r.status_code >= 400:
        return None

    discovery_doc_json = r.json()
    discovery_doc = OAuth2Config(
        issuer=discovery_doc_json['issuer'],
        auth_endpoint=discovery_doc_json['authorization_endpoint'],
        userinfo_endpoint=discovery_doc_json['userinfo_endpoint'],
        revoke_endpoint=discovery_doc_json['revocation_endpoint'],
        token_endpoint=discovery_doc_json['token_endpoint'],
        jwks_uri=discovery_doc_json['jwks_uri'])

    return discovery_doc


getDiscoveryDocument = get_discovery_document()
