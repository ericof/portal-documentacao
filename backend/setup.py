"""Installer for the ericof.docs package."""

from pathlib import Path
from setuptools import find_packages
from setuptools import setup


long_description = f"""
{Path("README.md").read_text()}\n
{Path("CONTRIBUTORS.md").read_text()}\n
{Path("CHANGES.md").read_text()}\n
"""


setup(
    name="ericof.docs",
    version="1.0.0a0",
    description="Projeto de portal de documentação utilizando Plone + Keycloak",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone CMS",
    author="Érico Andrei",
    author_email="ericof@plone.org",
    url="https://github.com/ericof/ericof.docs",
    project_urls={
        "PyPI": "https://pypi.org/project/ericof.docs",
        "Source": "https://github.com/ericof/ericof.docs",
        "Tracker": "https://github.com/ericof/ericof.docs/issues",
    },
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["ericof"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8",
    install_requires=[
        "setuptools",
        "Plone",
        "plone.api",
        "plone.restapi",
        "plone.volto",
        "plone.exportimport",
        "collective.glossary",
        "pas.plugins.oidc>=2.0.0b2",
        "pas.plugins.keycloakgroups",
    ],
    extras_require={
        "test": [
            "zest.releaser[recommended]",
            "zestreleaser.towncrier",
            "plone.app.testing",
            "plone.restapi[test]",
            "pytest",
            "pytest-cov",
            "pytest-plone>=0.5.0",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = ericof.docs.locales.update:update_locale
    """,
)
