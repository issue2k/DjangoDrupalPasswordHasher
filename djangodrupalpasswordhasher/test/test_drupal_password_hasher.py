if __name__ == '__main__' and __package__ is None:
    import os
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings.configure())

from drupal_password_hasher import DrupalPasswordHasher

