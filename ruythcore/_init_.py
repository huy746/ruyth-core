from .client import Client, RuythCore
from .context import Context
from .slash import SlashManager
from .command import PrefixCommandManager
from .http import HTTPClient
from .voice import VoiceManager
from .constants import DEFAULT_INTENTS

# Expose names at package level so users can:
# import ruythcore
# bot = ruythcore.Client("token")
__all__ = [
    "Client",
    "RuythCore",
    "Context",
    "SlashManager",
    "PrefixCommandManager",
    "HTTPClient",
    "VoiceManager",
    "DEFAULT_INTENTS",
]

__version__ = "1.0.0"
__author__ = "ruythbot_huy"
