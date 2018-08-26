import os


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cmdb.settings")

    import django
    django.setup()

    from app01 import models
