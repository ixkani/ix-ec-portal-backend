import django
from django.test.runner import DiscoverRunner
from django.conf import settings
from django.core.management import call_command
from django.db.utils import ConnectionHandler

class HerokuTestSuiteRunner(DiscoverRunner):
    def setup_databases(self, **kwargs):

        test_connections = ConnectionHandler(settings.TEST_DATABASES)

        for alias in django.db.connections:
            test_connection = test_connections[alias]

            django.db.connections[alias] = test_connection

            # re-initialize database (this "replaces" the CREATE DATABASE which
            # cannot be issued on Heroku)
            cursor = test_connection.cursor()
            cursor.execute('DROP SCHEMA public CASCADE')
            cursor.execute('CREATE SCHEMA public')

            # make them tables
            call_command('migrate',
                        verbosity=0,
                        interactive=False,
                        database=test_connection.alias,
                        load_initial_data=False)

            call_command('flush',
                verbosity=0,
                interactive=False,
                database=test_connection.alias)

            from django.core.cache import caches
            from django.core.cache.backends.db import BaseDatabaseCache
            for cache_alias in settings.CACHES:
                cache = caches[cache_alias]
                if isinstance(cache, BaseDatabaseCache):
                    call_command('createcachetable', cache._table,
                                 database=test_connection.alias)

    def teardown_databases(self, *args, **kwargs):
        pass