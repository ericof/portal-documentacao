from ericof.docs import logger
from ericof.docs import PACKAGE_NAME
from pathlib import Path
from plone import api
from plone.exportimport import importers
from Products.GenericSetup.tool import SetupTool

import os
import requests


EXAMPLE_CONTENT_FOLDER = Path(__file__).parent / "examplecontent"

KEYCLOAK_SERVICE = os.environ.get("KEYCLOAK_SERVICE", "http://sso.localhost")

OIDC_SETTINGS = {
    "issuer": f"{KEYCLOAK_SERVICE}/realms/plone",
    "client_id": "plone",
    "client_secret": "12345678",  # nosec B105
    "create_restapi_ticket": True,
    "redirect_uris": [
        "/login-oidc/oidc",
    ],
    "scope": ("openid", "profile", "email"),
}

KEYCLOAK_GROUPS = {
    "enabled": True,
    "server_url": KEYCLOAK_SERVICE,
    "realm_name": "plone",
    "client_id": "plone-admin",
    "client_secret": "12345678",  # nosec B105
}


def setup_keycloak(portal_setup: SetupTool):
    """Setup keycloak authentication."""
    portal = api.portal.get()
    oidc = portal.acl_users.oidc
    for key, value in OIDC_SETTINGS.items():
        setattr(oidc, key, value)
    logger.info("Configured pas.plugins.oidc")
    for key, value in KEYCLOAK_GROUPS.items():
        name = f"keycloak_groups.{key}"
        api.portal.set_registry_record(name, value)
    logger.info("Configured pas.plugins.keycloakgroups")


def create_example_content(portal_setup: SetupTool):
    """Import content available at the examplecontent folder."""
    portal = api.portal.get()
    importer = importers.get_importer(portal)
    for line in importer.import_site(EXAMPLE_CONTENT_FOLDER):
        logger.info(line)
    try:
        response = requests.get(KEYCLOAK_SERVICE, timeout=2)
        status = response.status_code
    except requests.exceptions.ConnectionError:
        status = 404
    if status < 399:
        logger.info("Configuring keycloak")
        portal_setup.runAllImportStepsFromProfile(f"{PACKAGE_NAME}:keycloak")
