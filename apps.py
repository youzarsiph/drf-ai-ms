""" Microservice AppConf """

from django.apps import AppConfig


# Create your AppConf here.
class DrfAiMsConfig(AppConfig):
    """App configuration for microservice"""

    name = "drf_ai_ms"
    default_auto_field = "django.db.models.BigAutoField"
