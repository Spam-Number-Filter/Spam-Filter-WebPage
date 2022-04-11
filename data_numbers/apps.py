""" File that contains all the apps from our project. """
from django.apps import AppConfig


class DatanumbersConfig(AppConfig):
    """Class that contains the spam number filter app from our project."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "data_numbers"
