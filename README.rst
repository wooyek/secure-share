============
Secure Share
============

A test project for job application


.. image:: https://img.shields.io/pypi/v/secure-share.svg
        :target: https://pypi.python.org/pypi/secure-share

.. image:: https://img.shields.io/travis/wooyek/secure-share.svg
        :target: https://travis-ci.org/wooyek/secure-share


.. image:: https://coveralls.io/repos/github/wooyek/secure-share/badge.svg?branch=develop
        :target: https://coveralls.io/github/wooyek/secure-share?branch=develop
        :alt: Coveralls.io coverage

.. image:: https://codecov.io/gh/wooyek/secure-share/branch/develop/graph/badge.svg
        :target: https://codecov.io/gh/wooyek/secure-share
        :alt: CodeCov coverage

.. image:: https://api.codeclimate.com/v1/badges/0e7992f6259bc7fd1a1a/maintainability
        :target: https://codeclimate.com/github/wooyek/secure-share/maintainability
        :alt: Maintainability

.. image:: https://img.shields.io/github/license/wooyek/secure-share.svg
        :target: https://github.com/wooyek/secure-share/blob/develop/LICENSE
        :alt: License

.. image:: https://img.shields.io/twitter/url/https/github.com/wooyek/secure-share.svg?style=social
        :target: https://twitter.com/intent/tweet?text=Wow:&url=https://github.com/wooyek/secure-share
        :alt: Tweet about this project

.. image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg
        :target: https://saythanks.io/to/wooyek


* Free software: MIT license


Features
--------

* Pending :D

Demo
----

To run an example project for this django reusable app, click the button below and start a demo serwer on Heroku

.. image:: https://www.herokucdn.com/deploy/button.png
    :target: https://heroku.com/deploy
    :alt: Deploy Django Opt-out example project to Heroku


Quickstart
----------

1. Fork the `secure-share` repo on `https://github.com/wooyek/secure-share`
2. Clone your fork locally::

    $ git clone git@github.com:wooyek/secure-share.git

3. Setup your development env::

    $ pipsi install pew
    $ cd secure-share/
    $ pew new -p python3 -a $(pwd) $(pwd | xargs basename)
    $ pew workon secure-share
    $ pip install -r requirements/development.txt

4. Test project health::

    $ python manage.py check
    $ pytest
    $ inv check
    $ tox

5. Initialize development database and fill it with test data::

    $ bash bin/database_create.sh
    $ inv db

6. Create a branch for local development and start development server::

    $ git checkout -b name-of-your-bugfix-or-feature
    $ python manage.py runserver


Deployment
----------

Add a development remote and deploy::

    $ git remote add dev https://git.heroku.com/secure-share-dev.git
    $ inv deploy

Credits
-------

This package was created with Cookiecutter_ and the `wooyek/cookiecutter-django-app`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`wooyek/cookiecutter-django-app`: https://github.com/wooyek/cookiecutter-django-app
.. _`pipenv`: https://docs.pipenv.org/install
.. _`Dokku PaaS`: http://dokku.viewdocs.io/dokku/getting-started/installation/
