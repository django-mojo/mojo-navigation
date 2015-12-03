.. image:: https://badge.fury.io/py/mojo-navigation.png
  :target: http://badge.fury.io/py/mojo-navigation
  :alt: PyPI version
  :height: 18px

.. image::  https://travis-ci.org/django-mojo/mojo-navigation.svg?branch=master
  :target: https://travis-ci.org/django-mojo/mojo-navigation
  :alt: build-status
  :height: 18px

.. image:: https://coveralls.io/repos/django-mojo/mojo-navigation/badge.svg?branch=master&service=github'
  :target: https://coveralls.io/r/django-mojo/mojo-navigation
  :alt: coverage
  :height: 18px


###############
MOJO NAVIGATION
###############

This Django app manages navigations trees with simple features. It is highly inspired by django-treenav and django-sitetree. It offers a lighter version to allow easy customisation.

The trees structure is using mptt. Each item offer various options to generate the url, restrict access given user status and permissions, classes and behaviours.


Changelist view:

.. image:: https://box.everhelper.me/attachment/342272/1VqyhRX5tQTX7AFhZZpY6HdPzrPh3QmW/341506-7MaquApmPbU02vSZ/screen.png
   :height: 400px
   :width: 800 px

Add view:

.. image:: https://box.everhelper.me/attachment/342274/1VqyhRX5tQTX7AFhZZpY6HdPzrPh3QmW/341506-JJ7ps4S6TNfi1DI6/screen.png
   :height: 400px
   :width: 800 px

Install
=======

It is strongly recommanded to install this theme from GIT with PIP onto you project virtualenv.

From PyPi

.. code-block::  shell-session

    pip install mojo-navigation

From Github

.. code-block::  shell-session

    https://github.com/django-mojo/mojo-navigation#egg=mojo-navigation

setup
=====

This application works with django mptt module in order to display the trees. It is highly recommended to add it in the INSTALLED_APPS.

.. code-block::  python

    INSTALLED_APPS = (
        ...
        'django_mptt'
        ...
    )

If you want to use the default model and admin, also install the module itself.

.. code-block::  python

    INSTALLED_APPS = (
        ...
        'mojo.navigation'
        ...
    )

Then install your model with

.. code-block::  shell

    python manage.py syncdb

In case you are using South, you can alternatively do:

.. code-block::  shell

    python manage.py migrate mojo.navigation

********
Managers
********

There are 2 main managers to help sortting and filtering the menu items.

Tree
====

You can get all items of a specific tree by passing its slug in the *for_tree* manager, for exemple:

.. code-block::  python

    tree_items = Item.objects.for_slug('slug_exemple')

User
====

As we are using permissions for items. You can filter items for a specific user to retrieve all the items he has access to by passing its object in the *for_user* manager, for exemple:

.. code-block::  python

    tree_items = Item.objects.for_user(request.user)

************
Contribution
************


Please feel free to contribute. Any help and advices are much appreciated.


*****
LINKS
*****

Github:
    https://github.com/django-mojo/mojo-navigation

Pypi:
    https://pypi.python.org/pypi/mojo-navigation
