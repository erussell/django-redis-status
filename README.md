django-memcache-status
========

This app displays the current load and some statistics for your redis-cache
instances in the index view of your Django admin section. It's tested with
*Django 1.3*

django-memcache-status is largely based on zalew/django-memcache-status, which
is itself a fork of bartTC/django-memcache-status


Installation
---------

Put ``redis_status`` in your ``INSTALLED_APPS``.

That's all. Only admin-users with ``superuser`` permission can see these stats.
