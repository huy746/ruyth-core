# ruythcore/__init__.py

from .client import Client, RuythCore
from .context import Context
from .slash import SlashManager
from .command import PrefixCommandManager
from .http import HTTPClient
from .voice import VoiceManager
from .constants import DEFAULT_INTENTS

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

# Attach module-level để import ruythcore.Client hoạt động
import sys
_module = sys.modules[__name__]
_module.Client = Client
_module.RuythCore = RuythCore
_module.PrefixCommandManager = PrefixCommandManager
_module.Context = Context
_module.SlashManager = SlashManager
_module.HTTPClient = HTTPClient
_module.VoiceManager = VoiceManager
_module.DEFAULT_INTENTS = DEFAULT_INTENTS

__version__ = "1.0.1"
__author__ = "ruythbot_huy"
